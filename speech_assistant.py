import speech_recognition as sr
import webbrowser
import time
from time import ctime
import pyttsx3


engine = pyttsx3.init()
r = sr.Recognizer()


def engine_speak(text):
    engine.say(text)
    engine.runAndWait()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak("I did not understand you")
        except sr.Requesterror:
            engine_speak("Sorry my service is down")
        return voice_data


def respond(voice_data):
    if "what is your name" in voice_data:
        engine_speak("My name is Imad")
    if "what time is it" in voice_data:
        engine_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you search for ?")
        url = "https://duckduckgo.com/?q=" + search
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search)
    if "find location" in voice_data:
        search = record_audio("Which place are you looking for ?")
        url = "https://google.com/maps/place/" + search
        webbrowser.get().open(url)
        engine_speak("Here is the location of " + search)
    if "goodbye" in voice_data:
        engine_speak("Goodbye !")
        exit()


time.sleep(1)
engine_speak("How may I help you ?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
