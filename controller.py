from Queue import Queue
import threading
from threading import Thread
from multiprocessing import Process
import time
import sys
import framework
import view
import getch
import json
import requests
import os
import pyaudio
import wave

# TODO: Heartbeat threading, bluemix integration, better structure.

keystrokes = Queue()
strings = Queue()

with open('credentials.json') as credential_file:
    credentials = json.load(credential_file)


def main():
    """Idles waiting for keystrokes. If key is escape, puts "esc" on keystrokes queue,
    which will initiate framework raising SystemExit. If key is enter, it should start a bluemix STT worker thread."""

    key = ord(getch())
    if key == 27:  # ESC
        keystrokes.put("esc")
    elif key == 13:  # Enter
        # TODO: Start a bluemix thread? Have to sort bluemix out first.
        # Probably a worker daemon though.
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

def record():
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "recording.wav"

    audio = pyaudio.PyAudio()
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    # print "recording..."
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

if __name__ == '__main__':
    #   Threading targets
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

    cProcess = Thread(target=_controllerstart, name='CONTROLLER')
    vProcess = Thread(target=_viewstart, name='VIEW')
    fProcess = Thread(target=_frameworkstart, name='FRAMEWORK')


    #Initialize and join
    cProcess.start()
    vProcess.start()
    fProcess.start()

    cProcess.join()
    vProcess.join()
    fProcess.join()
