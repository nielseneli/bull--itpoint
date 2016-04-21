from Queue import Queue
import threading
from threading import Thread
import time
import sys
import framework
import view
import bluemix
import getch
import json
import requests
import os

#TODO: Heartbeat threading, bluemix integration, better structure.

keystrokes = Queue()
strings = Queue()

with open('credentials.json') as credential_file:
    credentials = json.load(credential_file)

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

def bluemix(audio_input):
    """Should stream data through a bluemix session until enter keyup and
    recieve results, then return the most probable text as a string"""

    api_method = '/v1/recognize'
    url = credentials['url']
    POST_url = url+api_method
    header={'Content-Type': 'audio/wav'}
    payload = {'continuous':True, 'profanity_filter': False}

    response = requests.post(POST_url, auth=(credentials['username'], credentials['password']),headers=header,data=audio_input,params=payload)

    # print 'recieved'
    assert (response.status_code == 200)
    # print('status_code: {} (reason: {})'.format(response.status_code, response.reason))
    result = json.loads(response.text)
    return result['results'][0]['alternatives'][0]['transcript']
    # print 'done'

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
