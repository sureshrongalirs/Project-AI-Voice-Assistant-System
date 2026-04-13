import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser

#Taking the male voice from my system
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

#engine.say("Hello, I am your assistant. How can I help you?")
#engine.runAndWait()

def speak(text):
    """This function converts text to a voice

    Args:
        text
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()
    
#speak("Hello, I am your assistant. How can I help you?")

#This is logger for the application
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    return query

#text = takeCommand()
#print(text)
#speak(text)

#while True:
#    query = takeCommand()
#    speak(query)

def wish_me():
    hour = int(datetime.datetime.now().hour)
    #print(hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning! How are you doing today?")
    elif hour>12 and hour<18:
        speak("Good Afternoon! How are you doing today?")
    else:
        speak("Good Evening! How are you doing today?")
        
    speak("I am your assistant. Please tell me how can I help you?")
    
#wish_me()

while True:
    #wish_me()
    query = takeCommand()
    #speak(query)
    print(query)
    
    if "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
        
    # Small talk
    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")

    
    elif "who made you" in query:
        speak("I was created by system, a brilliant mind!")

    
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
    
    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")

    elif "exit" in query:
        speak("Good bye sir")
        exit()
        
    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")

    
    