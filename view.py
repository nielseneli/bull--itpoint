""" Contains the View part of the project. Has a Slide class, as well as
classes that inherit from that: Slide_List, Slide_Title, etc.
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def test_me():
	'''tests this script by creating a slide and updating it.
	Only for debugging use within this file.
	'''
	test_slide = Slide_Title(title='This is a title')
	test_slide.make_subtitle('This is a subtitle')
	return test_slide.update()
    # Uncomment to test List Slides instead
	# test_slide2 = Slide_List(title='This is a listy title', items=['hi','howdy'])
	# test_slide2.add_item('hey')
	# return test_slide2.update()

class SlideDeck(object):
	'''currently not in use. still being developed.'''
	def __init__(self):
		self.deck = []

	def addtoDeck(slide):
		self.deck.append(slide)


class Slide(object):
	""" Creates a Slide object. Has child classes Slide_List and Slide_Title.
	Theoretically, should never initialize this class -- always initialize a
	child class that is more specific for what kind of slide you need.
	"""

	def __init__(self):
		pass

	def update(self):
		""" Updates whatever visual we have so you can see everything currently
		on a slide.
		Should be overridden by more specific slides' update method for their
		own formatting. Currently just prints useless string to webpage if not overridden.
		"""
		#If this shows, you didn't create an actual specified slide. Go make a specific slide.
		return 'This slide has no content.'


class Slide_List(Slide):
    """ Inherits from Slide class. Can make a title and a list of items.
    """

    def __init__(self, title=None, items=None, image_url = None):
        '''Initially assigns optional title value and list of items to the object's attributes.
        May cause errors if given 'items' is not a list or 'title' is not a string.
        '''
        self.title = title
        if items is None:
            self.items = [] #sets items to an empty list if none are preset
        else:
            self.items = items #sets items if preset to that list. May cause errors if items is not a list.

	def update(self):
		"""Formats the list of items with Flask so it looks like a list and
		outputs to webpage. Calls separate file: slide_list_template.html
		"""
		# self.addtoDeck()
		return render_template('slide_list_template.html', title=self.title, items=self.items)

	def make_title(self, text):
		""" Takes in title text.
		Modifies self.title to match input text.
		"""
		self.title = text

    def make_list(self, items):
        """ Takes in list of items and sets it as items attribute.
        """
        self.items = items

    def add_item(self, new_item):
        """ Takes in new_items and adds it to self.items.
        """
        self.items.append(new_item)
    def add_image(self, image_url):
        """ Adds an image to the slide"""
        self.image_url = image_url


class Slide_Title(Slide):
	""" Inherits from Slide class. Can make a title and a subtitle for a title
	slide.
	"""

	def __init__(self, title=None, subtitle=None):
		'''Initially assigns optional title and subtitle values to the object's attributes.
		'''
		self.title = title
		self.subtitle = subtitle

	def update(self):
		""" Formats the title text with Flask so it looks like a title and
		outputs to webpage. Calls separate file: slide_title_tempmlate.html
		"""
		# self.addtoDeck()
		return render_template('slide_title_template.html', title=self.title, subtitle=self.subtitle)

	def make_title(self, text):
		""" Takes in title text.
		Modifies self.title to match input text.
		"""
		self.title = text

	def make_subtitle(self, text):
		""" Takes in subtitle text.
		Modifies self.subtitle to match input text.
		"""
		self.subtitle = text

if __name__ == '__main__':
	# enables debugging mode, so you don't have to restart
	# the server each time you change your code
	app.run(debug=True)
	test_me()
