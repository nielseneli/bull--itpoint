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


# How to Use

Upon keypress, the following commands will produce actions based on what you couple them with:

| Command | Output on Slide |
| ------- | ------ |
| "Today I am here to talk about..." | Creates title slide |
| "My name is..." | Adds "Presented by" subtitle to title slide |
| "Which brings us to..." | Creates new slide wtih specified title |
| "Next slide is about..." | Creates new slide wtih specified title |
| "Point..." | Adds bullet point to list |
| "Thing is..." | Adds bullet point to list |
| "Here's an image from Wolfram Alpha of..." | Inserts image from Wolfram Alpha |
| "Figure [One/Two/Three]" | Insert pre-loaded image from local directory |

