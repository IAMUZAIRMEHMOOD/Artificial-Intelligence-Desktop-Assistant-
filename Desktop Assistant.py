import pyttsx3 #pip install pyttsx3
import datetime #built in library
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser #built in
import os # for music
import smtplib #build in
########################################################################
#sapi5 Speech api buit in window
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[1].id)
#voices[1] or 2 gives male or female voice option
print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello! I am your Desktop Assistant.Please tell me how may i Help You")