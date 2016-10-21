# slAIdes

## What It Does
slAIdes is flexible presentation software. It creates a slide deck, in real time, while you present, encouraging more flexible presentation styles and more procrastination.

### Basic Code Structure:
slAIdes is written in Model-View-Controller form, with each component in a discrete file.
Each of these live on their own thread, with the controller initializing everything.
Data is passed between the controller and the framework on two queues, and the framework passes the view display objects.


## How to Use
Let's get started!

### How to Download
Press the "Download .zip" or "Download .tar.gz" button in the header on [our website](http://nielsenlouise.github.io/slAIdes/ "slAIdes") to download either a .zip  or a tar.gz of the software.

### How to Install
We're not sure about this yet.

#### Dependencies
Run:
```
$ pip install twisted autobahn requests pyOpenSSL flask getch
```
To run ```reveal.js```, you will also need to install it as seen on [reveal.js's readme](https://github.com/hakimel/reveal.js#full-setup), which is copied here for convenience:

1. Install Node.js (1.0.0 or later)

2. Install Grunt

3. Clone the reveal.js repository
    ```
    $ git clone https://github.com/hakimel/reveal.js.git
    ```
4. Navigate to the reveal.js folder
    ```
    $ cd reveal.js
    ```
5. Install dependencies
    ``` $ npm install ```
6. Serve the presentation and monitor source files for changes
    ```
    $ grunt serve
    ```
7. Open http://localhost:8000 to view your presentation

You may also need to run:
```
$ apt-get install build-essential python-dev
```
### How to Run
So start, simply run 'controller.py', eg:
```
python controller.py
```

#### Example code
Examples inbound soon.

## Code Structure
slAIdes is written in Model-View-Controller form. The model is written in `framework.py`, the view portion is written in `view.py`, and the controller portion is written in `controller.py`.

## Credits

### Team Members:

[Jared Briskman](https://github.com/jaredbriskman "Jared's Github profile")

[Margaret Crawford](https://github.com/Margaretmcrawf "Margo's Github profile")

[Lauren Gulland](https://github.com/laurengulland "Lauren's Github profile")

[Louise Nielsen](https://github.com/nielsenlouise "Louise's Github profile")

### License:

```
MIT License

Copyright (c) 2016 Jared Briskman, Margaret Crawford, Lauren Gulland, and Louise Nielsen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
