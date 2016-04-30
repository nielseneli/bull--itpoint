""" Contains the View part of the project. Has a Slide class, as well as
    classes that inherit from that: Slide_List, Slide_Title, etc. This branch
    is implementing reveal.js to render a presentation.
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
        """ Finds the insert cue, goes back two lines to account for formatting,
        then adds things.
        """
        with open('reveal.js-master/index.html', 'r+') as deck:
            deck_lines = deck.readlines()
            insert = deck_lines.index('\t\t\t\t<!-- insert here pls -->\n') - 2
            deck_lines.insert(insert, additional_text)
            deck.seek(0)
            deck.write(''.join(deck_lines))
            deck.truncate()


class Slide_List(SlideDeck):
    """ Inherits from SlideDeck class. Can make a title and a list of items.
    This can only add a title when it initializes.
    """

    def __init__(self, title='', items=None):
        """ Initially assigns optional title value and list of items to object's
        attributes and creates a slide with that title and those list items.
        """
        self.title = title
        if items is None:
            self.items = []
            self.add_slide('## ' + self.title + '\n')
        else:
            self.items = items
            items_str = '\n- '.join(self.items)
            self.add_slide('## ' + self.title + '\n\n- ' + items_str)

    def update_list(self, new_items):
        """ Takes in list of one or more items, sets it as items attribute, and
        updates index.html to present the updated slide.
        """
        self.items.extend(new_items)
        items_str = '\n- '.join(new_items)
        self.add_text_to_slide('- ' + items_str + '\n')


class Slide_Title(SlideDeck):
    # TODO: Implement this with reveal.js.
    """ Inherits from SlideDeck class. Can make a title and a subtitle. This
    can only add a title when it initializes.
    """

    def __init__(self, title='', subtitle=''):
        """ Initially assigns optional title and subtitle values to object's
        attributes and creates a slide with that title and subtitle.
        """
        self.title = title
        self.subtitle = subtitle
        if self.subtitle is '':
            self.add_slide('# ' + self.title + '\n\n')
        else:
            self.add_slide('# ' + self.title + '\n\n' + '### ' + self.subtitle + '\n')

    def add_subtitle(self, text):
        """ Takes in subtitle text.
        Modifies self.subtitle to match input text.
        """
        self.subtitle = text
        self.add_text_to_slide('### ' + text + '\n')

if __name__ == '__main__':
    trying = SlideDeck()
    current = Slide_Title(title='title slide pls')
    current.add_subtitle('does it work')
