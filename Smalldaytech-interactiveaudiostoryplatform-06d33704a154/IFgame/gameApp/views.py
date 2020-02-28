from django.shortcuts import render
import pyaudio
import wave
import requests
from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import pygame
import os
from playsound import playsound

import requests






k=1
def increment_func():
    global k
    k = k + 1
# Create your views here.

def game_homepage(request):

    return render(request,'gameApp/homepage.html')

def start_record(request):
    save_path='../Recordings/'
    my_path = os.path.abspath(os.path.dirname(__file__))
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5

    WAVE_OUTPUT_FILENAME =os.path.join(my_path+"/Recordings/'file"+str(k)+".wav")

    increment_func()
    audio = pyaudio.PyAudio()

    stream123 = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    waveFile123=wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    audio = pyaudio.PyAudio()
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream123=stream
    print("finished recording")

    waveFile123=waveFile
    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile123.setnchannels(CHANNELS)
    waveFile123.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile123.setframerate(RATE)
    waveFile123.writeframes(b''.join(frames))
    data=waveFile123
    #playsound(WAVE_OUTPUT_FILENAME)
    waveFile.close()
    print("stopped recording")
    return render(request,'gameApp/homepage.html',{'data' :'recording'})

def sample(request):
    url = 'http://dummy.restapiexample.com/api/v1/employees'
    data= url.json()


    return render(request, 'gameApp/sample.html', {
        'employee_salary': data['employee_salary'],

    })
