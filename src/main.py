import datetime
import os
import subprocess
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

# initialize text to speech
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)


def speak(audio):
    """ gives voice output from text """
    engine.say(audio)
    engine.runAndWait()
    pass


def listen():
    """ takes voice input from user """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # prevent statement completion while user is speaking with gaps
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query_res = r.recognize_google(audio, language="en-in")
    except Exception as e:
        print(e)
        print("Pardon..")
        return "None"
    return query_res.lower()


def greet():
    """ greets the user when the program starts """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 < hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How may i help you?")


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


if __name__ == '__main__':
    greet()
    while True:
        query = listen()
        print("User said: ", query)
        if 'good night' in query:
            speak("Bye bye!")
            exit(0)
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia," + results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open gmail' in query or 'show me my mails' in query:
            webbrowser.open("gmail.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'play music' in query:
            music_dir = '/home/aman/Music'
            songs = os.listdir(music_dir)
            open_file(os.path.join(music_dir, songs[0]))
