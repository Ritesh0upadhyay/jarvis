elif 'send message' in query:
            dm = takecommand().lower()
            r = int(takecommand().lower())
            

            kit.sendwhatmsg(f"{r}",f"{dm}")