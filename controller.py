from multiprocessing import Process, Queue
import time
import framework
import json
import requests
import pyaudio
import wave
import evdev

strings = Queue()
keystrokes = Queue()
device = evdev.InputDevice('/dev/input/event4')

with open('credentials.json') as credential_file:
    credentials = json.load(credential_file)


def main(strqueue, keyqueue):
    """ Idles waiting for keystrokes. If key is escape, puts "esc" on keystrokes
    queue, which will initiate framework raising SystemExit. If key is space,
    while space is held, records audio and then sends audio to Bluemix and adds
    the returned string to the strings queue.
    Takes in:
            strqueue: the queue that deals with text strings
            keyqueue: the queue that deals with keystrokes
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
                text = bluemix(audio)
                strqueue.put(text)
                # print to the command line so you can see if Bluemix messed up
                print text


def bluemix(audio_input):
    """ Streams data through a bluemix session until enter keyup and
    recieve results, then returns the most probable text as a string.
    Takes in:
            audio_input: the .wav file containing speech to interpret
    """
    api_method = '/v1/recognize'
    url = credentials['credentials']["url"]
    POST_url = url+api_method
    header = {'Content-Type': 'audio/wav'}
    payload = {'continuous': True, 'profanity_filter': False}
    response = requests.post(POST_url, auth=(credentials['credentials']['username'], credentials['credentials']['password']), headers=header, data=audio_input, params=payload)
    assert (response.status_code == 200)
    result = json.loads(response.text)
    return result['results'][0]['alternatives'][0]['transcript']


def record():
    """ Records audio while the space bar is pressed and saves the audio to
    recording.wav. """
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    WAVE_OUTPUT_FILENAME = "recording.wav"

    audio = pyaudio.PyAudio()
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
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
    # Initialize the queues
    # strings = Queue()
    # keystrokes = Queue()
    # Define process targets
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
    # Initialilze processes
    cProcess = Process(target=_controllerstart, args=((strings),(keystrokes),), name='CONTROLLER')
    fProcess = Process(target=_frameworkstart, args=((strings),(keystrokes),), name='FRAMEWORK')
    # Start and join processes
    cProcess.start()
    fProcess.start()

    cProcess.join()
    fProcess.join()
