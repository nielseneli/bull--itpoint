import json
import requests
import os
import pyaudio
import wave


with open('credentials.json') as credential_file:
    credentials = json.load(credential_file)['credentials']

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
    RECORD_SECONDS = 1
    WAVE_OUTPUT_FILENAME = "recording.wav"

    audio = pyaudio.PyAudio()
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print "recording..."
    frames = []
    try:
        while True:
            # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
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

record()
filepath = '/home/jwb/Documents/git/slaides/recording.wav'  # path to file
audio = open(filepath,'rb').read()
print bluemix(audio)
