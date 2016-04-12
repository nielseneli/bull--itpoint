""" This is the framework part of our interactive slide project. It will take a string input
from the speech-to-text, process it and make a slide object."""
import view.py
from controller.py import strings, keystrokes #names subject to change
import time

while True: #loop continues checking for new strings until we make it quit with a keystroke
	
	strings.get()

	#the following section is for creating a new slide
	if 'title slide' in string:
		slide = Slide_Title() #make new title slide
	elif 'list slide' in string:
		slide = Slide_List() #make new list slide

	#TODO: think about the optimal way to do this. Like maybe a dictionary instead
	#of a bunch of if statements because eventually there will be a lot of things here and 
	#it won't be very readable
	if 'the title of this slide is' in string: 
		title = string.split('the title of this slide is', 1)[1]
		slide.title = title
	elif 'bullet' in string:
		bullet = string.split('bullet', 1)[1]
		slide.add_item(bullet)

	if keystrokes.pop() == 'esc':
		break

	time.sleep(.01) #allow the other threads to work
