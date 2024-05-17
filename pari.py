import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
from requests import get
import cv2
import time
import pyjokes
import sys
from selenium import webdriver
import requests
import pywikihow 
import winsound
import urllib.request
import numpy as np
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir !")

    else:
        speak("Good Evening sir !")

    speak("I am your Mili.")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    
    speak("Lemme know your name")
   


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print("Say that again please...")
        speak("say that again please")
        return "None"
    query = query.lower()
    return query
def body():
    
    wishMe()
    while True:
        query = takeCommand()

        if 'pari' in query or 'sambhavi' in query or 'pandey ji' in query or'sam' in query or 'panda' in query:
            speak('Hello ,,, Pari my sir likes you and he ordered me to do this when i hear your name.')
           

        else:
            speak('Hello sir, or mam i dont know you letme confirm it with my database or you can talk to my sir')


if __name__ == "__main__":
    speak("please speak the password")
    while True:
        m1 = takeCommand()
        if "i am here" in m1:
            body()
        else:
            speak("sory sir the password is not correct")
        