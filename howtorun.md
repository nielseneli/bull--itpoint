---
title: Running Bull--it Point
layout: template
filename: howtorun
---


## Basic Code Structure:

Bull--itPoint is written in Model-View-Controller form, with each component in a discrete file.

Each of these live on their own thread, with the controller initializing everything.

Data is passed between the controller and the framework on two queues, and the framework passes the view display objects.

# How to Use

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

### How to Run

So start, simply run `controller.py`, eg:

```
python controller.py
```

