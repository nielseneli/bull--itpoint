# Preparation and Framing

#### slAIdes

## Background and context

slAIdes is intended to be flexible presentation software. You present verbally and the software creates a slide deck that corresponds with your speech.

Currently, our code is made of three parts.

#### `controller.py`

`controller.py` is what recognizes keystrokes, records audio, and feeds the audio to Bluemix.

#### `framework.py`

`framework.py` checks for new strings from `controller.py`, searches for images and other similar things, and creates and calls slide methods from `view.py`.

#### `view.py`

`view.py` contains the definitions of classes `SlideDeck`, `Slide`, and specific types of slides (e.g. `Slide_List` and `Slide_Title`).

## Key questions

## Agenda for technical review session
