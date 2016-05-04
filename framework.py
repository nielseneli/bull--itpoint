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
slideDeck = view.SlideDeck('slidedeck')

strings = ['create title slide', 'the title of this slide is cool shit']
keystrokes = ['not quit']

slide = view.Slide_List()

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
            current = 
        if 'create title slide' in text:

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
        elif 'heres an image from wolfram alpha of' in text:
            searchterm = text.split('heres an image from wolfram alpha of')[1]
            slide.add_image(get_wolframalpha_imagetag(searchterm)['src'], get_wolframalpha_imagetag(searchterm)['alt'])
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