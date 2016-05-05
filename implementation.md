---
title: Implementation Details
layout: template
filename: implementation
---

# How is Bull--itPoint Implemented?

## Technologies
*IBM BlueMix
*Reveal.js
*Wolfram Alpha API
*XML Trees
*Queues

## Dependencies
something

##Overview
The code is comprised of three major parts, in a model-view-controller setup. The overall process takes audio input on a keypress, which is then processed by IBM's BlueMix speech-to-text. The text is then processed by our framework, which makes API calls to Wolfram Alpha, finds images from the local directory, or parses text based on keywords. The slides are then created in reveal.js and loaded to the presentation. *something something threading something something

## Controller
Controller initializes the other functions, and uses keyboard input from (*some keypress technology???*). 
It uses this to start recording audio with (*some package or other*) and then gets Bluemix to transcribe it as text. The text is then sent to a queue which is then used by framework.

## Framework
The framework is divided into two functions:
main:
This function takes the queue from controller.py and parses the strings, then writes things to view.
get_wolfram_imagetag:
This function takes a searchterm and calls the Wolfram API, then parses the resulting xml tree for an image and returns the url source.

## View
This defines the objects to be used in the other functions and the methods for updating the reveal.js slideshow. The basic object is a slide deck, which must be initialized before creating any slides. Then there are two types of slide-- title slides and list slides. Each have different methods


Code doesn't tell a story by itself. Use more effective methods such as flowcharts and architectural or class diagrams to explain how your code works. You could consider including or linking to snippets of code to highlight a particularly crucial segment.
