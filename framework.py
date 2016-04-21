""" This is the framework part of our interactive slide project. It will take a
    string input from the speech-to-text, process it and make a slide object.
"""
import view
from controller import strings, keystrokes
import sys
import requests

#functions for APIs and things
def get_image_url('searchterm'):
	API_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q='
	+ searchterm.replace(' ', '%20')
	r = requests.get(API_URL)
	return json.loads(r.text)['responseData']['results']['unescapedUrl'] #the url for the first image

# loop continues checking for new strings until user keystrokes
def main():
    for text in strings.get()
#       the following section is for creating a new slide
        if 'create title slide' in text:
            slide = view.Slide_Title() # make new title slide
            slide.update()
        elif 'create list slide' in text:
            slide = view.Slide_List()  # make new list slide
            slide.update()

#	This section calls slide methods when certain phrases are found in the string

        if 'the title of this slide is' in text:
            title = text.split('the title of this slide is', 1)[1]
            slide.title = title
            slide.update()
        elif 'point' in text:
            bullet = text.split('point', 1)[1]
            slide.add_item(bullet)
            slide.update()
        if 'add image of' in text:
        	searchterm = text.split('add image of')[1]
        	url = get_image_url(searchterm)
        	slide.add_image(url)
        	slide.update()

#if the escape key is pressed, that will be sent to the keystroke queue which will quit the program.
    for key in keystrokes.get():
        if keystrokes.pop() == 'esc':
            sys.quit