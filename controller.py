import threading
from threading import Thread
from multiprocessing import Process, Queue
import time
import sys
import framework
import view
# import getch
import json
import requests
import os
import pyaudio
import wave
import evdev

# TODO: Heartbeat threading, bluemix integration, better structure.

keystrokes = Queue()
strings = Queue()
device = evdev.InputDevice('/dev/input/event4')

with open('credentials.json') as credential_file:
    credentials = json.load(credential_file)


def main(strqueue, keyqueue):
    """ Idles waiting for keystrokes. If key is escape, puts "esc" on keystrokes
    queue, which will initiate framework raising SystemExit. If key is enter,
    it should start a bluemix STT worker thread.
    """
    keys = device.active_keys()
    if keys:
        for key in keys:
            if key == 1:  # ESC
                keyqueue.put("esc")
            elif key == 57:  # Space bar
                record()
                filepath = 'recording.wav'  # path to file
                audio = open(filepath,'rb').read()
                stuff = bluemix(audio)
                # stuff = 'today I am here to talk about pancakes'
                # stuffs = 'which brings us to maple syrup'
                strqueue.put(stuff)
                # queue.put(stuffs)
                print stuff


def bluemix(audio_input):
    """Should stream data through a bluemix session until enter keyup and
    recieve results, then return the most probable text as a string"""

    api_method = '/v1/recognize'
    url = credentials['credentials']["url"]
    POST_url = url+api_method
    header = {'Content-Type': 'audio/wav'}
    payload = {'continuous': True, 'profanity_filter': False}

    response = requests.post(POST_url, auth=(credentials['credentials']['username'], credentials['credentials']['password']), headers=header, data=audio_input, params=payload)

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
    while 57 in device.active_keys():
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
    _running = True
    #   Threading targets

    strings = Queue()
    keystrokes = Queue()

    def _frameworkstart(strqueue, keyqueue):
        try:
            global _running
            while _running:
                framework.main(strqueue, keyqueue)
                time.sleep(.01)
        except SystemExit:
            _running = False

    def _controllerstart(strqueue, keyqueue):
        global _running
        while _running:
            main(strqueue, keyqueue)
            time.sleep(.01)

    cProcess = Process(target=_controllerstart, args=((strings),(keystrokes),), name='CONTROLLER')
    fProcess = Process(target=_frameworkstart, args=((strings),(keystrokes),), name='FRAMEWORK')


    # Initialize and join
    cProcess.start()
    fProcess.start()

    cProcess.join()
    fProcess.join()
