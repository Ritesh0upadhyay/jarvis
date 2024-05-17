def account_info():
    with open('info.txt')
elif 'hide my file' in query or "hide this folder" in query or "visible to everyone" in query:

            speak("Sure sir please tell again if  you want to hide or unhide the files")
            condition = takecommand().lower()
            if'hide' in condition:
                {
                    os.system("attrib  +h /s /d")
                    speak("sir,all the files in this folder are now hidden")
                }
            elif'visible' in condition:
                {
                    os.system("attrib  -h /s /d")
                    speak("sir ,all the files in this foldet are now visible to everyone ,i think that you have done it without any pressure")
                }
            elif 'leave it' in condititon or "leave for now" in condition:
                {
                    speak("Ok sir ")
                }

from selenium.webdriver.chrome.options import options
from bs4 import Beautifulsoup





    while True:
        permission = takeCommand()
        if 'wake up'in permission:
            TaskExecution()
        elif 'sleep jarvis' in permission or 'goodbye' in permission:
            speak("thanks,for using me sir have a nice day and please call me if you need me")
            sys.exit()   



               elif 'send message' in query:
            speak("sir what should i write in the message")
            msz = takeCommand()

            from twilio.rest import client

            account_sid = 'AC218f8ff628a463307dd84b4973b20ac3'
            auth_token = '1299adbab6d0205372b2c442e9739c38'

            client = Client(account_sid, auth_token)

            message = client.messages \
               .create(
                   body = msz,
                   From = "+18455391561"
                   to = "+916375123855"
               )
            print(message.sid)


        elif 'please call' in query:
            speak("sir please wait i am calling ")
        

            from twilio.rest import client

            account_sid = 'AC218f8ff628a463307dd84b4973b20ac3'
            auth_token = '1299adbab6d0205372b2c442e9739c38'

            client = Client(account_sid, auth_token)

            message = client.calls \
               .create(
                   twiml='<Response><Say>This is the testion message from jarvis side ..</Say></Response>'
                   from = '+18455391561'
                   to = '+916375123855'
               )
            print(message.sid)




             elif 'set alarm' in query:
            nm = int(datetime.datetime.now().hour)
            a=int(intput("enter the time in hours 24 hrs format"))
            if nm==a:
                music_dir = "c:\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))