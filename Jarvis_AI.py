import pyttsx3
#pip install pyttsx3
import speech_recognition as sr
#pip install speechRecognition
import datetime
import wikipedia
#pip install wikipedia for wikipedia used
import webbrowser
# for google stackoverflow and youtube
import os
# for music
import smtplib
# for email uses
import random

engine = pyttsx3.init('sapi5')
#hmri window ak api lati hoti hay or ya voices ko detect karay gi
voices = engine.getProperty('voices')
# print(voices[1].id) computer ma basically 2 voices hoti hian by default male or female
# print(voices[1].id)
engine.setProperty('voice', voices[0].id) # for set which voice is used


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!\n")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!\n")
        speak("Good Afternoon!")

    else:
        print("Good Evening!\n")
        speak("Good Evening!")

    print("Welcome Back I am Jarvis Sir. Please tell me how may I help you?\n")
    speak("Welcome Back I am Jarvis Sir. Please tell me how may I help you? ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # come from speekrecognization module
        audio = r.listen(source)

    try:
        # use jb hamain lagta hay error aaa skty hain
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":

    print("What is Your Name? ")
    speak("What is Your Name? ")
    query2 = takeCommand().lower()
    if 'dawood' in query2:
        wishMe()
        while True:
        #if 1:
            query = takeCommand().lower()
        # convert query in lower case after passing through takecommand

        # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                # kitna data chahiya depend upon sentences
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                music_dir = 'F:\\Songs'
                songs = os.listdir(music_dir)
                print(songs)
                b = random.randint(1,100)
                os.startfile(os.path.join(music_dir, songs[b]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
                os.startfile(codePath)

            elif 'stop' in query:
                print("Good Bye")
                speak("Good bye")
                False

            # elif 'quit' in query:
            #     False

            # elif 'email to Saad' in query:
            #     try:
            #         speak("What should I say?")
            #         content = takeCommand()
            #         to = "SaadyourEmail@gmail.com"
            #         sendEmail(to, content)
            #         speak("Email has been sent!")
            #     except Exception as e:
            #         print(e)
            #         speak("Sorry my friend Saad bro. I am not able to send this email")
    else:
        print("You are not my Owner")
        speak("You are not my Owner")