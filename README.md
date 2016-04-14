# slAIdes

##IMPORTANT: SlAIdes is not in a working state currently. Development is active, and working builds will be tagged.

## What It Does
slAIdes is flexible presentation software. It creates a slide deck, in real time, while you present, encouraging more flexible presentation styles and more procrastination.

### Basic Code Structure:
slAIdes is written in Model-View-Controller form, with each component in a discrete file.
Each of these live on their own thread, with the controller initializing everything.
Data is passed between the controller and the framework on two queues, and the framework passes the view display objects.


## How to Use
Let's get started!

### How to Download
Press the "Download .zip" or "Download .tar.gz" button in the header to download either a .zip  or a tar.gz of the software.

### How to Install
I don't know this either.

#### Dependencies
Run:
```
$ pip install twisted autobahn requests pyOpenSSL flask getch
```
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
slAIdes is written in Model-View-Controller form.

### Model
The model is written in `framework.py`.

### View
The view portion is written in `view.py`.

### Controller
The controller portion is written by `controller.py`.

## Credits

### Team Members:

[Jared Briskman](https://github.com/jaredbriskman "Jared's Github profile")

[Margaret Crawford](https://github.com/Margaretmcrawf "Margo's Github profile")

[Lauren Gulland](https://github.com/laurengulland "Lauren's Github profile")

[Louise Nielsen](https://github.com/nielsenlouise "Louise's Github profile")
