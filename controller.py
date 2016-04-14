from Queue import Queue
import threading
from threading import Thread
import time
import sys
import framework
import view
import getch

#TODO: Heartbeat threading, bluemix integration, better structure.

keystrokes = Queue()
strings = Queue()

def main():
    """Idles waiting for keystrokes. If key is escape, puts "esc" on keystrokes queue,
    which will initiate framework raising SystemExit. If key is enter, it should start a bluemix STT worker thread."""
    key = ord(getch())
    if key == 27: #ESC
        keystrokes.put("esc")
    elif key == 13: #Enter
        #TODO: Start a bluemix thread? Have to sort bluemix out first.
        #Probably a worker daemon though.
        strings.put(bluemix())

def bluemix():
    """Should stream data through a bluemix session until enter keyup and
    recieve results, then return the most probable text as a string"""
    pass
    #Bluemix returns a JSON object, with text as an element

if __name__ == '__main__':
    #Threading targets
    def _frameworkstart():
        try:
        	global _running
        	while _running:
        		framework.main()
                time.sleep(.01)
        except SystemExit:
    		_running = False

    def _controllerstart():
    	global _running
    	while _running:
    		main()
            time.sleep(.01)

    def _viewstart():
    	global _running
    	while _running:
    		view()

    cThread = Thread(target=_controllerstart, name='CONTROLLER')
    vThread = Thread(target=_viewstart, name='VIEW')
    fThread = Thread(target=_frameworkstart, name='FRAMEWORK')


    #Initialize and join
    cThread.start()
    vThread.start()
    fThread.start()

    cThread.join()
    vThread.join()
    fThread.join()
