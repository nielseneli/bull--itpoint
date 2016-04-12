""" Contains the View part of the project. Has a Slide class, as well as
classes that inherit from that: Slide_List, Slide_Title, etc.
"""


class Slide(object):
    """ Creates a Slide object. Has child classes Slide_List and Slide_Title.
    """

    def __init__(self):
        pass

    def update(self):
        """ Updates whatever visual we have so you can see everything currently
        on a slide.
        Should be overridden by more specific slides' update method for their
        own formatting. Currently just prints to terminal if not overridden.
        """
        print 'This slide has no content.'


class Slide_List(Slide):
    """ Inherits from Slide class. Can make a list of items.
    """

    def __init__(self, title='', items=None):
        self.title = title
        if items is None:
            self.items = []
        else:
            self.items = items

    def update(self):
    	"""Formats the list of items with Flask so it looks like a list and
        outputs to webpage.
        """
        # TODO: Implement with Flask
        # For now, this prints to terminal
        for i in len(self.items):
            print str(i + 1) + '. ' + self.items[i]

    def make_list(self, items):
        """ Takes in list of items.
        """
        self.items = items
        self.format_list()
        self.update()

    def add_item(self, new_item):
        """ Adds a new item to self.items.
        """
        self.items.append(new_item)


class Slide_Title(Slide):
    """ Inherits from Slide class. Can make a title and a subtitle for a title
    slide.
    """

    def __init__(self, title='', subtitle=''):
        self.title = title
        self.subtitle = subtitle

    def update(self):
        """ Formats the title text with Flask so it looks like a title and
        outputs to webpage.
        """
        # TODO: Implement with Flask
        # For now, this prints to terminal.
        print self.title
        print self.subtitle

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
