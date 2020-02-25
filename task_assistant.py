import pyttsx3 
import datetime
import speech_recognition as sr
import os
import wolframalpha
import pyaudio
import wikipedia
import webbrowser
import sys
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    ''' this function is used for wish user'''

    hour = int(datetime.datetime.now().hour)
    if hour < 12 :
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")


def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresold = 1
        # here audio variable is requied to store the input because we want to recognize that
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in") # here the "l" of "language" is must be in lower case 
        print("user said",query)

    except Exception as e:

        print("I can't recognize your command please type it")
        speak("I can't recognize your command please type it")
        query = input("enter your command  ")
        return query

    return query


def task():

    ''' this function is used for take command from user and performe task according that '''
	
    query = take_command().lower()

    if "google" in query:
        speak("okay sir")
        webbrowser.open("google.com")

    elif "youtube" in query:
        speak("okay sir")
        webbrowser.open('youtube.com')

    elif "hello" in query:
        speak("hello sir")

    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))

    elif 'bye' in query:
        speak('Bye Sir, have a good day.')
        sys.exit()

    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak('okay')
        speak('Bye Sir, have a good day.')
        sys.exit()

    elif "wikipedia" in query:
        speak("searching in wikipedia...")
        query = query.replace("wikipedia"," ")
        result = wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(result)
        speak(result)
    elif "yes" in query:
        return True
    elif "no" in query:
        return False
    else:
        return query

def speak_():

    query = take_command().lower()
    return  query

if __name__ == '__main__':
    wishMe()
    task()