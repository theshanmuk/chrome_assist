import pyttsx3
import speech_recognition as sr
import webbrowser as wb
chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
i=0
def chromes():
        with sr.Microphone() as source:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say("say someting to search, shanmuk")
            engine.runAndWait()
            r = sr.Recognizer()
            r.energy_threshold = 4000
            audio = r.listen(source)
            engine.say("ok!")
            engine.runAndWait()
            try:
                text = r.recognize_google(audio)
                print(text)
            except:
                pass

            l1 = list(text.split())
            if "open" in l1:
                l1.remove("open")
            if "search" in l1:
                l1.remove("search")
            if"about" in l1:
                l1.remove("about")
            str = ""
            c = "opening..." + str.join(l1)
            print(c)
            engine.say(c)
            engine.runAndWait()
            if ".com" in text:
                e=str.join(l1)
                wb.get(chrome).open(e)
            d = "https://google.com/search?q=" + str.join(l1) + "&rlz=1C1GCEA_enIN857IN857&oq=sha&aqs=chrome.0.69i59j69i57j0l2j69i61l2.5386j0j7&sourceid=chrome&ie=UTF-8"
            wb.get(chrome).open(d)
chromes()
def move():
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say("do you want to search again?")
        engine.runAndWait()
        engine.say("say yes or no")
        engine.runAndWait()
        r = sr.Recognizer()
        r.energy_threshold = 4000
        audio = r.listen(source)
        engine.say("ok!")
        engine.runAndWait()
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            pass
        i = 0
        if "yes" in text:
            while i == 0:
                chromes()
                move()
        if "no" in text:
            exit(0)
move()












