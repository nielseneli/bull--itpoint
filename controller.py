from Queue import Queue
import threading
from threading import Thread
import sys
import framework
import view
import getch

keystrokes = Queue()
strings = Queue()

def main():
    #TODO: Bluemix and getch onto the queues.

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
