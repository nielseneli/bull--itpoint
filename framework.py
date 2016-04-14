""" This is the framework part of our interactive slide project. It will take a
    string input from the speech-to-text, process it and make a slide object.
"""
import view
from controller import strings, keystrokes
import sys

# loop continues checking for new strings until user keystrokes
def main():
    for text in strings.get()
#       the following section is for creating a new slide
        if 'title slide' in text:
            slide = view.Slide_Title() # make new title slide
            slide.update()
        elif 'list slide' in text:
            slide = view.Slide_List()  # make new list slide
            slide.update()

#	This section calls slide methods when certain phrases are found in the string
#   TODO: think about the optimal way to do this. Like maybe a dictionary with functions
#   instead of a bunch of if statements because eventually there will be a lot
#   of things here and it won't be very readable

        if 'the title of this slide is' in text:
            title = text.split('the title of this slide is', 1)[1]
            slide.title = title
            slide.update()
        elif 'bullet' in text:
            bullet = text.split('bullet', 1)[1]
            slide.add_item(bullet)
            slide.update()

#if the escape key is pressed, that will be sent to the keystroke queue which will quit the program.
    for key in keystrokes.get():
        if keystrokes.pop() == 'esc':
            sys.quit
