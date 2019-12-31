import pyttsx3 #pip install pyttsx3
import datetime #built in library
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser #built in
import os # for music
import smtplib #build in
#pip install pyaudio
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
     phrase = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         phrase.pause_threshold = 1
         audio = phrase.listen(source)

     try:
         print("Recognizing..")
         query = phrase.recognize_google(audio,language='en-pk')
         #query = phrase.recognize_google(audio,Language='en-pk')
         print("User said: "+query)
         #print(f"User said:{query} \n" ) #back string use
     except Exception as e:
         print(e)
         print("Say that again please...")
         return"None"
     return query
def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('from@gmail.com','Password Here')
     server.sendmail('from@gmail.com',to,content)
     server.close()

if __name__ == "__main__":
     wishme()
     while True:
         query = takeCommand().lower() 
         if 'open wikipedia' or 'open wiki' or 'open pedia' or 'open wiki pedia'in query:
             webbrowser.open("wikipedia.com")
         #Logic for executing tasks based on query
         elif  'search wikipedia' or 'search wiki pedia' or 'wiki pedia' or 'wkipedia'in query:
             speak("searching Wikipedia...")
             query = query.replace("Wikipedia","")             
             results = wikipedia.summary(query,sentences=3)
             speak("According to Wikipedia")
             print(results)
             speak(results)
         elif 'open stackoverflow' or 'open stack overflown' or 'open stack over flown'in query:
             webbrowser.open("stackoverflow.com")
         elif 'open youtube' or 'open you tube' or 'youtube' or 'you tube'in query:
             webbrowser.open("youtube.com")
         elif 'open google' or 'google now' or 'open search' in query:
             webbrowser.open("google.com")
         elif 'play music' or 'lets play music' or 'play music' in query: 
             music_dir = 'M:\\Music\\Songs\\Milli'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[0]))
         elif 'the time' or 'time' or 'what is the time' or 'time right now' or 'time right now?' or 'what time is it' or 'or what time is it?' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak("Sir the time is"+ strTime)
             #speak(f"Sir, the time is {strTime}")
         elif 'open vscode' or 'open vs code' or 'vs code open' or 'vs code' or 'vs code' in query:
             codepath = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
             os.startfile(codepath)
         elif 'email myself' or 'email' or 'send email' or 'sent email' in query:
             try:
                 speak("What should i say")
                 content = takeCommand()
                 to = "to@gmail.com"
                 sendEmail(to,content)
                 speak("Email has been sent")
             except Exception as e:
                 speak("Sorry my Friend.Email cannot be send")
         elif 'open dropbox' or 'open drop box' or 'dropbox' or 'drop box' in query:
             codepath = 'C:\\Program Files (x86)\\Dropbox\\Client\\Dropbox.exe'
         elif 'open ccleaner' or 'open cleaner' or 'open c cleaner' or 'c cleaner' or 'ccleaner' or 'cleaner' in query:
             codepath = 'C:\\Program Files\\CCleaner\\CCleaner64.exe'
         elif 'open eclipse' or 'eclipse' or 'e clipse' or 'open e clipse' in query:
             codepath = 'C:\\eclipse\\eclipse.exe'
         elif 'open mozilla' or 'open firefox' or 'open mozilla firefox' or 'open fire fox' or 'firefox' or 'firefox' in query:
             codepath = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
         elif 'open foxit reader' or 'open reader' or 'open foxit' or 'foxit' or 'foxit reader' or 'reader' in query:
             codepath = 'C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\Foxit Reader\\FoxitReader.exe'
         elif 'open google chrome' or 'open chrome' or 'google chrome' or 'chrome' in query:
             codepath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
         elif 'open hp photosmart essential' or 'open photosmart' or 'open photo smart' or 'open photosmart essential' in query:
             codepath = 'C:\\Program Files (x86)\\HP\\Digital Imaging\\bin\\hpqpse.exe'
         elif 'open hp solution center' or 'open hp ' or 'open solution center' or 'solution center' in query:
             codepath = 'C:\\Program Files (x86)\\HP\\Digital Imaging\\bin\\Hpqdirec.exe'
         elif 'open microsoft edge' or 'Open edge' or 'edge' or 'microsoft edge' in query:
             webbrowser.open()
         elif 'open netbeans' or 'open net beans' or 'open net bean' or 'open netbean' or 'netbeans' or 'net beans'in query:
             codepath = 'C:\\Program Files\\NetBeans 8.2\\bin\\netbeans64.exe'
         elif 'open notepad ++' or 'open notepad plus plus' or 'open notepad plusplus' or 'notepad plus plus' or 'notepad ++' in query:
             codepath = 'C:\\Program Files (x86)\\Notepad++\\notepad++.exe'
         elif 'open team viewer' or 'team viewer' in query:
             codepath = 'C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe'
         elif 'open vlc media player' or 'open vlc' or 'vlc' or 'open media player' in query:
             codepath = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
         elif 'open vmware workstation pro' or 'open vmware' or 'open workstation' or 'open vm ware' or 'open v m ware' or 'vmware' or 'vm ware' or 'v m ware' in query:
              codepath = 'C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe'
         elif 'adobe creative cloud' or 'open abobe creative cloud' or 'open creative cloud' or 'creative cloud' in query:
              codepath = 'C:\\Program Files (x86)\\Adobe\\Adobe Creative Cloud\\ACC\\Creative Cloud.exe'
         elif 'open google backup' or 'google backup' or 'open google backup and sync' or 'open backup and sync' or 'backup and sync' or 'backup and sync from google' in query:
              codepath = 'C:\\Program Files\\Google\\Drive\\googledrivesync.exe'
         elif 'open packet tracer' or 'packet tracer' or 'open tracer' or 'open packet' in query:
              codepath =  'C:\\Program Files (x86)\\Cisco Packet Tracer 7.2\\bin\\PacketTracer7.exe'
         elif 'open lightroom' or 'lightroom' or 'open light room' or 'light room' in query:
              codepath = 'C:\\Program Files\\Adobe\\Adobe Lightroom CC\\lightroomcc.exe'
         elif 'open opera' or 'opera' in query:
              codepath = 'C:\\Program Files\\Adobe\\Adobe Lightroom CC\\lightroomcc.exe'
         elif 'open c s' or 'open cs' or 'open cs1.6' or 'open cs 1.6' or 'open counter strike' or 'c s' or 'cs' or 'cs1.6' or 'cs 1.6' or 'counter strike' in query:
              codepath = 'C:\\Games\\Cs 1.6 Original\\cstrike.exe'
         elif 'open one drive' or 'open onedrive' or 'one drive' or 'onedrive' in query:
              codepath = 'C:\\Users\\uzair\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe'
         elif 'open call of duty sigle player' or 'open cod' or 'open c o d' or 'open call of duty single' or 'open cod single player' or 'open c o d single player' or 'call of duty sigle player' or 'cod' or 'c o d' or 'call of duty single' or 'cod single player' or 'c o d single player' in query:
              codepath = 'C:\\Games\\Call of Duty Modern Warfare\\iw3sp.exe'
         elif 'open call of duty multi player' or 'open call of duty multi' or 'open cod multi player' or 'open c o d multi player' or 'call of duty multi player' or 'call of duty multi' or 'cod multi player' or 'c o d multi player' in query:
              codepath = 'C:\\Games\\Call of Duty Modern Warfare\\iw3mp.exe'
         elif 'open cricket 7' or 'open cricket seven' or 'open cricket' or 'open cricket 07' or 'cricket 7' or 'cricket seven' or 'cricket' or 'cricket 07' in query:
              codepath = 'C:\\Games\\EA Sports Cricket 2007\\Cricket07.exe'
         elif 'open strike fighter' or 'open janes strike fighter' or 'strike fighter' or 'janes strike fighter' in query:
              codepath = 'C:\\Games\\Janes Advanced Strike Fighters\\JASF.exe'
         elif 'open wire shark' or 'open wireshark' or 'wireshark' or 'wire shark' in query:
              codepath = 'C:\\Program Files\\Wireshark\\Wireshark.exe'
         elif 'open controlpanel' or 'open control panel' or 'control panel' or 'control panel' in query:
              codepath = 'C:\\Users\\uzair\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk'
         elif 'open cmd' or 'open c m d' or 'open command prompt' or 'cmd' or 'c m d' or 'command prompt' in query:
              codepath = 'C:\\Users\\uzair\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk'
         elif 'open file explorer' or 'open file xplorer' or 'file explorer' or 'file xplorer' in query:
              codepath = 'C:\\Users\\uzair\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.Ink'
         elif 'open run' or 'run' in query:
              codepath = 'C:\\Users\\uzair\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run.Ink'
         elif 'open my computer' or 'open this pc' or 'this pc' or 'my computer' in query:
              codepath = 'C:\\Users\\uzair\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\This PC.lnk'
         else :
             speak("Your Command is not Recognized")
