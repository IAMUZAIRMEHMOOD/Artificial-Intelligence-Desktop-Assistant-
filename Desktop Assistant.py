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
    def takeCommand():
        #It takes microphone input from user and returs string output 

     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,Language='en-pk')
        print(f"User said: {query}\n")#back string use
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return"None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
 
        #Logic for executing tasks based on query
        if  'wikipedia' in query:
                speak("searching Wikipedia...")
                query = query.replace("Wikipedia","")
                results = wikipedia.summary(query,sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
                webbrowser.open("google.com")

        elif 'open google' in query:
                webbrowser.open("stackoverflow.com")
        elif 'play music' in query: 
                music_dir = 'C:\\GulHameed\\Music\\Songs\\Favorite'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
