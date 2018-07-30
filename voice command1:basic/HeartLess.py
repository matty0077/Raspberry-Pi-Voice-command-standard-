import random, pickle, os
import os.path
from Mind import *
from datetime import datetime
t = datetime.now().strftime('%k %M')

#//////////////////////////////////////////////////////////////
def response(a):
    print("google supposes you said " + a)

    # the letter 'a' thruoghout this file
    #represents what the program thinks you said
    
        
    if "quit" in a:
        exit()
        
    #basic commands tied to functions
    if "calculate" in a :
        ROOK.calc()

    if "what time is it" in a:
        ROOK.say('time is %s'%t)

    if "search" in a:
        ROOK.browse()

    if "paint" in a:
        ROOK.paint()

    if "music" in a:
        ROOK.Music()
        
    if "who are you" in a:
        ROOK.say("I am "+ ROOK.NAME + " and you are " + ROOK.USER)
        ROOK.say('silly')

    if "#" in a:
        a = ""
 
while True:
    print("listening...")                          #c920    44100        512
    r = sr.Recognizer()                             #usb mic 16000      #128
    m=sr.Microphone(device_index = 1, sample_rate = 16000, chunk_size = 128)
    with m as source:
        r.adjust_for_ambient_noise(source, duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.energy_threshold = 1250#175#400
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        with open("memory/sounds/records/microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        audio.pause_threshold = 0.65
    try:
        a=r.recognize_google(audio)     
        print(a)                    
    except sr.UnknownValueError:
        ROOK.say("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        ROOK.say("You're not connected for whatever reason...lets try again")

