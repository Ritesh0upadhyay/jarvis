if __name__ == "__main__":
    speak("please speak the password")
    while True:
        m1 = takeCommand()
        if "i am here" in m1:
            body()
        else:
            speak("sory sir the password is not correct")
        