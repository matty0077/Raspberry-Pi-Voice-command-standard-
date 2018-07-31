import random, pickle, os
import os.path
import speech_recognition as sr
from espeak import espeak
import time
import random
import cgi,cgitb,sys
cgitb.enable()
from datetime import datetime
t = datetime.now().strftime('%k %M')

#///////////////#name self n save otherwise
def namesake():#change the names list or add to it for more variety
    names=['Kenneth','77','Rook','Tobio','Delta','Capricorn','Saint','i-selerian','Hal','Humphreys','Zir-Al-Mega','Zero','Friender','Amuro','Hector','Alpha','Hubris']
    NAME=names[random.randint(0,len(names)-1)]
    fi=open("/home/pi/Desktop/NAVI/SPIRIT/Voice Command/voice command1:basic/memory/ID/name.txt", "w")#"a"
    fi.write("\n" + NAME)
    fi.close()
    return NAME

#/////////////////////////////////////////////load name if exists 
def loadname():
    file=open("/home/pi/Desktop/NAVI/SPIRIT/Voice Command/voice command1:basic/memory/ID/name.txt", "r")
    Name=file.read()
    if Name!="":
        return Name
    else:
        namesake()

NAME=loadname() + "_5E"

#//////////////////////////////////////////////////////////////
def say(something):
    try:
        import subprocess                           #v voice       #s rate     p pitch   a volume
        voice1=subprocess.Popen(["espeak", "-v", "mb-en1","-s","117","-p","190","-a","80", something])                
    except Exception as e:
        print(e.message)
        
#/////////////////////
def response(a):
    # the letter 'a' thruoghout this file
    #represents what the program thinks you said
        
    if "quit" in a:
        exit()
        
    #basic commands tied to functions
    if "calculate" in a :
        say('math')
        from BASIC import calculator

    if "what time is it" in a:
        say('time is %s'%t)


    if "search" in a:
        say('what would you like to look up?')
        google = input('Google search:')
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)
        #remove_tab to open new window

    if "paint" in a:
        say('lets paint')
        from BASIC import paint
        
    if "who are you" in a:
        say("I am "+ NAME + " silly")

    if "#" in a:
        a = ""
        
 #///////////////////////
while True:
    #print("listening...")                          #c920    44100        512
    r = sr.Recognizer()                             #usb mic 16000      #128
    m=sr.Microphone(device_index = 1, sample_rate = 44100, chunk_size = 512)
    with m as source:
        r.adjust_for_ambient_noise(source, duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.energy_threshold = 1250#175#400
        print('listening...')
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        with open("memory/sounds/records/microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        audio.pause_threshold = 0.65
    try:
        a=r.recognize_google(audio)     
        print(a)
        response(a)
    except sr.UnknownValueError:
        say("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        say("You're not connected for whatever reason...lets try again")

