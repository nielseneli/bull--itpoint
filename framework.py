""" This is the framework part of our interactive slide project. It will take a
    string input from the speech-to-text, process it and make a slide object.
"""
import view
#from controller import strings, keystrokes
import sys
import requests
from flask import Flask
from flask import render_template


app = Flask(__name__)

strings = ['create title slide', 'the title of this slide is cool shit']
keystrokes = ['not quit']

slide = view.Slide_List()

#functions for APIs and things
def get_image_url(searchterm):
    API_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q='
    + searchterm.replace(' ', '%20')
    r = requests.get(API_URL)
    return json.loads(r.text)['responseData']['results']['unescapedUrl'] #the url for the first image

# loop continues checking for new strings until user keystrokes
@app.route('/')
def main():
    global slide
    if strings:
        text = strings.pop(0)
        #       the following section is for creating a new slide
        if 'create title slide' in text:
            print 'hit'
            slide = view.Slide_Title() # make new title slide
            return slide.update()
        elif 'create list slide' in text:
            slide = view.Slide_List()  # make new list slide
            return slide.update()

    #   This section calls slide methods when certain phrases are found in the string

        if 'the title of this slide is' in text:
            title = text.split('the title of this slide is', 1)[1]
            slide.make_title(title)
            return slide.update()
        elif 'point' in text:
            bullet = text.split('point', 1)[1]
            slide.add_item(bullet)
            return slide.update()
        elif 'add image of' in text:
            searchterm = text.split('add image of')[1]
            url = get_image_url(searchterm)
            slide.add_image(url)
            return slide.update()
    

    #if the escape key is pressed, that will be sent to the keystroke queue which will quit the program.
        for key in keystrokes:
            if keystrokes.pop() == 'esc':
                sys.quit

    return slide.update()
if __name__ == '__main__':
    # enables debugging mode, so you don't have to restart
    # the server each time you change your code
    app.run(debug=True)
    while True:
        main()