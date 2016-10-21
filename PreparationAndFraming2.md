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

#### Thoughts on basic code structure?

See the UML diagram in our [presentation](https://docs.google.com/presentation/d/1DlfqaEcr_wdShOdshvnxHDBXG5xGzTC51VTlze0of84/edit?usp=sharing 'Technical Review 2').

#### Thoughts on current problems?

Current problems include:

- threading and cohesiveness between Model, View, and Controller in real time
- dynamically loading Flask page (should be obsolete after transition to HackerSlides)

#### Thoughts on HackerSlides?

See [their website](https://sandstorm.io/news/2015-02-17-hacker-slides 'HackerSlides').

## Agenda for technical review session

You can read look for more detail in our [presentation](https://docs.google.com/presentation/d/1DlfqaEcr_wdShOdshvnxHDBXG5xGzTC51VTlze0of84/edit?usp=sharing 'Technical Review 2').

#### Overview of current project

#### Expansion plans

#### Demo
