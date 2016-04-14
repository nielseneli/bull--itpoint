---
title: Implementation Details
layout: template
filename: implementation
---

# How Did We Implement slAIdes?

## You'll never know, still a work in progress. But in the meantime, we have something here...

### Basic framework
Tell it to listen --> speech to text --> recognize key phrases --> make slide --> view slide

Eventually, there will probably be an image here.

#### Controller
Currently, the controller and the Bluemix speech to text are both located in `controller.py`. It does a bunch of things and I don't really know the details. Probably none of us know the details, it is not fully implemented yet.

#### Model
`framework.py` is called by `controller.py` when a keystroke indicates speech to text should be listening. `framework.py` looks for specific phrases in the text transcribed from the user and calls `view.py` to create a slide.

#### View
`view.py` contains several classes, probably more than there are now, and I do not remember all of the current ones anyway. It is called by `framework.py` to create and load (word?) a slide using Flask.

###### Original Instructions/Ideas Given By Teaching Team
Code doesn't tell a story by itself. Use more effective methods such as flowcharts and architectural or class diagrams to explain how your code works. You could consider including or linking to snippets of code to highlight a particularly crucial segment.
