import pyttsx3 
import datetime
import speech_recognition as sr
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)

def speak(audio):
	
	engine.say(audio)
	engine.runAndWait()

def wishMe():

	hour = int(datetime.datetime.now().hour)
	if hour < 12 :
		speak("Good Morning")

	elif hour >= 12 and hour < 18:
		speak("Good Afternoon")

	else:
		speak("Good Evening")

def take_command():

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_thresold = 1
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language="en-in")
		print("user said",query)

	except Exception as e:

		print("please say that again...")
		return "None"

	return query



if __name__ == '__main__':

	wishMe()
	print(take_command())