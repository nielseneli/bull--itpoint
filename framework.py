""" This is the framework part of our interactive slide project. It will take a
    string input from the speech-to-text, process it and make a slide object.

    Commands: 
    "Today I'm here to talk about BLANK": initializes a new title slide, titled BLANK.
    "Which brings us to BLANK": initializes new slide that can contain a bulleted list, titled BLANK.
    "point"/"thing is": Creates a new bulllet point item. Note, it only matters what you say after the keyword, so if you were to say "My first
    point is BLANK" or "another important thing is BLANK" 
    "Here's an image from Wolfram Alpha of BLANK": Makes a call to the Wolfram Alpha API, and pulls up an image of the thing.
    "Figure 1"/"Figure 2"/"Figure 3": Displays user's own images. These images must be put in the user's directory before the presentation
    and should be labeled figure1.jpg etc.

"""
import view
#from controller import strings, keystrokes
import sys
import requests
from flask import Flask
from flask import render_template


app = Flask(__name__)
slide_deck = view.SlideDeck('slidedeck')

strings = ['today i am here to talk about']
keystrokes = ['not quit']

slide = slideDeck.Slide_List() #if nothing is called fist just make random list slide

#functions for APIs and things
def get_wolframalpha_imagetag(searchterm):
    """ Used to get the first image tag from the Wolfram Alpha API. The return value is a dictionary
    with keys that can go directly into html."""
    base_url = 'http://api.wolframalpha.com/v2/query?'
    app_id = credentials['wolframkey'] #api key
    url_params = {'input':searchterm, 'appid':app_id}
    headers = {'User-Agent':None}
    data = urllib.urlencode(url_params)
    req = urllib2.Request(base_url, data, headers)
    xml = urllib2.urlopen(req).read()
    tree = ET.fromstring(xml)
    for e in tree.findall('pod'):
        for item in [ef for ef in list(e) if ef.tag=='subpod']:
            for it in [i for i in list(item) if i.tag=='img']:
                if it.tag == 'img':
                    if float(it.attrib['width']) > 50 and float(it.attrib['height']) > 50:
                        return it.attrib

# loop continues checking for new strings until user keystrokes
def main():
    global slide
    if strings:
        text = strings.pop(0)
        #       the following section is for creating a new slide
        if 'today i am here to talk about' in text:
            current = Slide_Title(title=text.split('today i am here to talk about')[1])
        elif 'which brings us to' in text:
            current = Slide_List(title=text.split('which brings us to')[1])

    #   This section calls slide methods when certain phrases are found in the string
        elif 'point' in text:
            bullet = text.split('point', 1)[1]
            current.update_list([bullet])
        elif "thing is" in text:
            bullet = text.split('thing is', 1)[1]
            current.update_list([bullet])
        elif 'heres an image from wolfram alpha of' in text:
            searchterm = text.split('heres an image from wolfram alpha of')[1]
            current.add_image(get_wolframalpha_imagetag(searchterm)['src'], get_wolframalpha_imagetag(searchterm)['alt'])
        elif 'figure one' in text:
            current.add_image('figure1.jpg')
        elif 'figure two' in text:
            current.add_image('figure2.jpg')
        elif 'figure three' in text:
            current.add_image('figure3.jpg')
    

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