""" Contains the View part of the project. Has a Slide class, as well as
    classes that inherit from that: Slide_List, Slide_Title, etcself.
    This branch is implementing reveal.js to render a presentation.
"""


class SlideDeck(object):
    """ The SlideDeck object is the index.html file in the reveal.js-master
    folder. When a new SlideDeck object is initialized, it copies index.copy in
    the slAIdes folder. It is necessary to run SlideDeck.end when the
    presentation is complete to save a copy of index.html to preserve the
    slidedeck for later use.
    """
    def __init__(self, filename='presentation'):
        """ Initializes the SlideDeck object by defining the filename for
        eventually saving the presentation and writes index.html in the
        reveal.js-master directory to begin the slideshow.
        """
        self.filename = filename
        with open('reveal.js-master/index.html', 'w') as deck:
            with open('index.copy', 'r') as f:
                read_data = f.read()
            deck.write(read_data)

    def add_text(self, text):
        """ Inserts text at the text-insert cue, which is always after the
        previous slide. The text-insert cue is hardcoded into index.copy but
        can be changed (is currently \t\t\t\t<!-- insert here pls -->\n)
        """
        with open('reveal.js-master/index.html', 'r+') as deck:
            deck_lines = deck.readlines()
            insert = deck_lines.index('\t\t\t\t<!-- insert here pls -->\n')
            deck_lines.insert(insert, text)
            deck.seek(0)
            deck.write(''.join(deck_lines))
            deck.truncate()

    def add_slide(self, slide_text):
        """ Adds a slide with the correct html formatting to be a markdown
        slide. slide_text is just plain text; more formatting, specific to
        types of slides, must be provided. Calls SlideDeck.add_text().
        """
        formatting = '\t\t\t\t<section data-markdown>\n\t\t\t\t\t<script type ="text/template">\n\t\t\t\t\t\t'
        formatting2 = '\n\t\t\t\t\t</script>\n\t\t\t\t</section>\n'
        self.add_text(formatting + slide_text + formatting2)

    def end(self):
        """ Saves the index.html file as self.filename + .html, currently in
        the slAIdes folder instead of the reveal.js-master folder.
        """
        with open(self.filename + '.html', 'w') as new_file:
            with open('reveal.js-master/index.html', 'r') as f:
                index_contents = f.read()
            new_file.write(index_contents)

    def add_text_to_slide(self, additional_text):
        # TODO: Implement this.
        """ Finds the insert cue, goes back two lines, then adds things.
        """
        pass


class Slide(object):
    """ I'm fairly certain this is completely unnecessary.
    """
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


class Slide_List(SlideDeck):
    # TODO: Finish implementing this with reveal.js.
    """ Inherits from Slide class. Can make a title and a list of items.
    """

    def __init__(self, title='', items=None):
        '''Initially assigns optional title value and list of items to the object's attributes.
        May cause errors if given 'items' is not a list or 'title' is not a string.
        '''
        self.title = title
        # sets items to an empty list if none are preset
        if items is None:
            self.items = []
        # sets items if preset to that list
        # ay cause errors if items is not a list
        else:
            self.items = items

    def update(self):
        """Formats the list of items with Flask so it looks like a list and
        outputs to webpage. Calls separate file: slide_list_template.html
        """
        items_str = '\n- '.join(self.items)
        self.add_slide('# ' + self.title + '\n\n- ' + items_str)


    def make_list(self, items):
        """ Takes in list of items and sets it as items attribute.
        """
        self.items = items
        self.update

    def add_item(self, new_item):
        """ Takes in new_items and adds it to self.items.
        """
        self.items.append(new_item)
        self.update


class Slide_Title(Slide):
    # TODO: Implement this with reveal.js.
    """ Inherits from Slide class. Can make a title and a subtitle for a title
    slide.
    """

    def __init__(self, title='', subtitle=''):
        '''Initially assigns optional title and subtitle values to the object's attributes.
        '''
        self.title = title
        self.subtitle = subtitle

    def update(self):
        """ Formats the title text with Flask so it looks like a title and
        outputs to webpage. Calls separate file: slide_title_tempmlate.html
        """
        self.addtoDeck()
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
    # app.run(debug=True)

    trying = SlideDeck()
    trying.add_slide('hey')
    current = Slide_List(title='list slide pls', items=['um', 'sure', 'k','mybe'])
    current.update()
    # current.make_list(['hey', 'not a very good fish at all'])
