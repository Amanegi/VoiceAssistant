import pyttsx3
import speech_recognition as sr

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
        query = r.recognize_google(audio, language="en-in")
        print("User said....", query, "\n")
    except Exception as e:
        print(e)
        print("Pardon..")
        return "None"
    return query


def greet():
    """ greets the user when the program starts """
    speak("Hello! How may i help you?")
    listen()


if __name__ == '__main__':
    greet()
