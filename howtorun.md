---
title: Running Bull--it Point
layout: template
filename: howtorun
---


# Basic Code Structure:

Bull--itPoint is written in Model-View-Controller form, with each component in a discrete file.

Each of these live on their own thread, with the controller initializing everything.

Data is passed between the controller and the framework on two queues, and the framework passes the view display objects.

# Initial Set-Up

Let's get started!

## How to Download

Press the "Download .zip" or "Download .tar.gz" button in the header to download either a .zip  or a .tar.gz of the software.

## How to Install

Still figuring this out!

### Dependencies

Run:

```
$ pip install twisted autobahn requests pyOpenSSL flask
```

You may also need to run:

```
$ apt-get install build-essential python-dev
```

## How to Run

To start, simply run `controller.py`, eg:

```
python controller.py

```
Commands: 
	```
    "Today I'm here to talk about BLANK": initializes a new title slide, titled BLANK.
    ```

    ```
    "Which brings us to BLANK/"next slide is about BLANK": initializes new slide that can contain a bulleted list, titled BLANK.
    ```

    ```
    "point"/"thing is": Creates a new bulllet point item. Note, it only matters what you say after the keyword, so if you were to say "My first point is BLANK" or "another important thing is BLANK" 
    ```

    ```
    "Here's an image from Wolfram Alpha of BLANK": Makes a call to the Wolfram Alpha API, and pulls up an image of the thing.
    ```

    ```
    "Figure 1"/"Figure 2"/"Figure 3": Displays user's own images. These images must be put in the user's directory before the presentation and should be labeled figure1.jpg etc.
    ```

# How to Use

Upon keypress, the following commands will produce actions based on what you couple them with:

| Command | Output |
| ------- | ------ |
| "Today I am here to talk about" | Creates title slide |
| "Which brings us to" | Creates list slide |
| "Next slide is about" | Creates list slide |
| "Point" | Adds bullet point to list |
| "Thing is" | Adds bullet point to list |
| "Here's an image from Wolfram Alpha of" | Inserts image from Wolfram Alpha |
| "Figure [One/Two/Three]" | Insert pre-loaded image from local directory |

