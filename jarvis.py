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
    speak(f"Its  {strTime}")
    speak("Lemme know how may I help you")
   

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


def askmyday():
    speak("how was your day sir ")
    q=takecommand()
    if 'it was fine' in q or 'it was good jarvis' in q:
        speak("that's very good sir,so now how can i help you")
    elif 'it was horible' in q or 'it was bad' in q or 'bad' in q:
        speak("no problem sir,now i wish all good things happens with you,so how can i help you sir")
    
def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    
    altime = altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done,alarm is set for {Timing} sir..")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.Playsound("abc".winsound.SND_LOOP)
            elif Mireal<datetime.datetime.now().minute:
                break

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('enjeenierritesh1234@gmail.com', 'rocking_jr.ritesh')
    server.sendmail('enjeenierritesh1234@gmail.com.a', to, content)
    server.close()

def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=68c5407067e54798adf62b5bc2c5a75f"
    main_page = requests.get(main_url).json()
    article = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"] 
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is:{head[i]}")

def search_wikihow(query,max_results=10,lang="en"):
    return list(Wikihow.search(query,max_result,lang))



def abs(a):
    "same as abs(abs)."
    return _abs(a)

def add(a,b):
    "same as a + b."
    return a + b
def and_(a,b):
    "same as a & b."
    return a & b

def floordiv(a,b):
    "same as a // b."
    return a // b

def index(a):
    "same as a.__index__()."
    return a.__index__()

def abs(a):
    "same as abs(abs)."
    return _abs(a)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def body():
    
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir,what shouls i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'open GeeksForGeeks' in query:
            webbrowser.open("geeksforgeeks.org")      


        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\VS code\\jarvis\\jarvis.py"
            os.startfile(codePath)

        elif 'mail to NSP' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "jr.ritesh6375123855@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")
        elif 'open notepad' in query:
            speak("opening notepad sir please wait  ")
            path = "%windir%\\system32\\notepad.exe"
            os.startfile(path)
        elif 'open camera' in query:
            
            cap = cv2.VedioCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam', img)
                h = cv2.waitkey(50)
                if (h==27):
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")
        
       
        elif 'sleep jarvis' in query:
            speak("thankyou sir have a nice day and please let me know if you have any work for me")
            sys.exit()


        elif 'close notepad' in query:
            speak("closing notepad sir,")
            speak("sir,do you have any work please tell me")
            os.system("taskkill /f /im notepad.exe")

       
        
        elif 'jokes' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'shut down' in query:
            os.system("shutdown /s /t S")
        elif 'restart' in query:
            os.system("shutdown /r /t S")
        elif 'news' in query:
            speak("please wait sir,fetching the latest news")
            news()
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
           
            pyautogui.keyUp("alt")

        elif 'take screenshot' in query:
            pyautogui.keypress(prtSc)
        
            

        elif " thankyou jarvis" in query:
            speak("its my pleasure ,sir to help you")
        
     
        
        elif " do some calculation " in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what tou want to calculate,example:3 plus 3")
                print("listening......")
                r.adjust_for_ambient_noice(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'devided' : operator.__truediv__,
                     }[op]
            def eval_binary_expr(op1,oper,op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split()))) 

        elif 'temperature' in query:
            search = "temperature in jaipur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").txt
            speak(f"current{search} is {temp}")
        elif 'hello jarvis' in query:
            speak("hello sir,how are you ,and how can i help you")
        elif 'i want to know about me' in query or 'i want to know about your sir and his family' in query:
            speak("what or who you want to know")
            know = takeCommand()
            speak(f"ok sir ,please wait a while let me search {know} in  my database")
            if 'about your sir' in know or 'about yourself' in know:
                speak("his name is Ritesh upadhyay,and he is in btec first year and he is currently working on me")
            elif 'about your sir father' in know:
                speak("my boss father name is mister vishwanath upadhyay,he is manager of  bharat pottries ")
            elif 'about your sir mom' in know:
                speak("my boss mother's name is misses Gudiya upadhyay and she is a house wife ")
            elif 'about your sir sister' in know:
                speak("my boss has two sister the elder one is Ritu upadhyay,she is a student of honours and the younger sister is ritika upadhyay she is a 11 class arts student")
            elif 'about your sir friends' in know:
                speak("my boss does not have many friends .he has 3 friend  at home and the others are college friends and they can be called as professional friends ")
            elif 'who is addarsh' in know:
                speak("he is my boss younger brother and he is now in my boss house")
        elif 'activate how to do mod' in query:
            from pywikihow import search_wikihow
            speak("sir,how to mode is activated please tell me what you want to know")
            while True:
                how = takeCommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("okay sir ,closing how to do mode")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir i am not able to get your voice")
        
        elif 'how much battery is left' in query or 'power' in query or 'battery' in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system has {percentage} percent battery left")
            if percentage>=75:
                speak("sir we can work ,and we have enough power to work")
            elif percentage>=40 and percentage<=30:
                speak("sir we should work ,but it will be good if we connect the charger")
            elif percentage>=15 and percentage<30:
                speak("sir we dont have enough power,i suggest you to plug system in charge")
            elif percentage<15:
                speak("we have a low power ,please connect to charging the system will soon shutdown")

        elif 'internet speed' in query:
            import speedtest
            speak("checking speed sir ,please wait..")
            st = speedtest.Speedtest()
            dl = st.download()
            d2 = dl/(1024*1024)
    
            up = st.upload()
            up2 = up/(1024*1024)
        
            speak(f"sir we have {d2} MB per second downloading speed and {up2} MB per second uploading speed")
        elif 'close camera' in query:
            speak("closing camera sir ,please wait")
            pyautogui.keypress(Esc)
        elif 'what is the festival jarvis' in query:
            speak("its holi sir ,by the way happy holi")

     

        elif 'change volume' in query:
            import pyautogui
            speak("sir what should i do")
            vm = takeCommand()
            if 'volume up' in vm:
                pyautogui.press("volumeup")
            elif 'volume down' in vm:
                pyautogui.press("volumedown")
            elif ' mute' in vm:
                pyautogui.press("volumemute")
        elif 'set alarm' in query:
            speak("sir please tell me the time to set alarm .for example : set alarm to 21:50 ")
            tt = takeCommand()
            tt = tt.replace("set alarm to ","")
            tt = tt.replace(".","")
            ttt = tt.upper()
            import myalarm
            MyAlarm.alarm(tt)

        elif 'open mobile camera in laptop' in query:
           
            speak("opening mobile camera sir please wait")
            URL = "http://<no_ip_address>:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.vint8)
                img = cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitkey(1)
                if q == ord("q"):
                    break;         

            cv2.destroyAllWindows()

        elif 'who is uday uncle' in query:
            speak("he lives in your house on rent ") 
        elif'who is kanak 'in query:
            speak("she is a baby girl and she lives in the corner house of my boss and this is the new of the important thing that  i ")
        elif'abuse' in query:
            speak("sir your all enemies including sisters are all chutiyaas")




z
if __name__ == "__main__":
    speak("please speak the password")
    while True:
        m1 = takeCommand()
        if "i am here" in m1:
            body()
        else:
            speak("sory sir the password is not correct")
        
        
        




            



















































































