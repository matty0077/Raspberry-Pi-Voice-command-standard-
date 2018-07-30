import speech_recognition as sr
from espeak import espeak
import time
import random
import cgi,os,cgitb,sys
cgitb.enable()
###//////////////////////// 
class ROOK():
        
#//////////////////////////////////////////////speak module
    def say(something):

        try:
            import subprocess                           #v voice       #s rate     p pitch   a volume
            voice1=subprocess.Popen(["espeak", "-v", "mb-en1","-s","117","-p","190","-a","80", something])
            ROOK.say(something)
                    
        except Exception as e:
            print(e.message)
    #/////////////////////////////////////////////load name if exists 
    def loadname():
        file=open("/memory/name.txt", "r")
        Name=file.read()
        if Name!="":
            return Name
        else:
            namesake()
    #///////////////#name self n save otherwise
    def namesake():#change the names list or add to it for more variety
        names=['Kenneth','77','Rook','Tobio','Delta','Capricorn','Saint','i-selerian','Hal','Humphreys','Zir-Al-Mega','Zero','Friender','Amuro','Hector','Alpha','Hubris']
        NAME=names[random.randint(0,len(names)-1)]
        fi=open("/memory/name.txt", "w")#"a"
        fi.write("\n" + NAME)
        fi.close()
        return NAME

    NAME=loadname() + "_4A"
    #/////////////////////////////////////////////load user name if exists 
    def loaduser():
        file=open("/memory/username.txt", "r")
        user=file.read()
        if user!="":
            return user
        else:
            saveuser()
    #///////////////#ask name n save otherwise
    def saveuser():
        USER=input(NAME +': so whats yer name?')
        fi=open("/username.txt", "w")#"a"
        fi.write("\n" + USER)
        fi.close()
        return USER

    USER=loaduser()

    def calc():
        ROOK.say('math')
        from BASIC import calculator

    def browse():
        ROOK.say('what would you like to look up?')
        google = input('Google search:')
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)
        #remove_tab to open new window

    def paint():
        ROOK.say('lets paint')
        from BASIC import paint
     
    def Music():
        ROOK.say('shuffling music')
        from BASIC import music
        
