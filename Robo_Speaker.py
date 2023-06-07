#import the module for voices
import pyttsx3

#initialize the engine
engine = pyttsx3.init()
#set the rate of 150 wpm
engine.setProperty('rate',150)
#set the voices
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
#make a loop that asks user untill user type q.
while True:
        x=input("What do you want me to say?:\n").lower()
        if x=="q":
            break
        engine.say(x)
        engine.runAndWait()


