""" This is the framework part of our interactive slide project. It will take a string input
from the speech-to-text, process it and make a slide object."""
import view.py

speech_strings = []
while True: #loop continues checking for new strings until we make it quit with a keystroke
	
	#TODO: get string from speech to text
	newstring = 
	speech_strings.append(newstring)

	string = speech_strings.pop([0])

	#the following section is for creating a new slide
	if 'title slide' in string:
		#make new title slide
		slide = Slide_Title()
	elif 'list slide' in string:
		#make new list slide
		slide = Slide_List()

#TODO: think about the optimal way to do this. Like maybe a dictionary instead
#of a bunch of if statements because eventually there will be a lot of things here and 
#it won't be very readable
	if 'the title of this slide is' in string: 
		title = string.split('the title of this slide is', 1)[1]
		slide.title = title
	elif 'bullet' in string:
		bullet = string.split('bullet', 1)[1]
		slide.add_item(bullet)
