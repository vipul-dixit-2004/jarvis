import os
import random
try:
    import speech_recognition as sr
except:
    print("Speech Recognition Module not found tryin to install...")
    os.system("pip install speechRecognition")
    import speech_recognition as sr
import webbrowser
import datetime
import time
try:
    import pyttsx3
    import wikipedia 
except:
    print("Pyttsx3 Module not found tryin to install...")
    os.system("pip install pyttsx3 wikipedia")
    import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
    #check for operating system

class voicebox:
    def speak(self,audio):
        self.audio = audio
        engine.say(audio)
        engine.runAndWait()

    #wishme
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning Sir")

        elif hour>=12 and hour<18:
            self.speak("Good Afternoon Sir")   

        else:
            self.speak("Good Evening Sir")  

        self.speak("getting all the data ready. PLease Wait.... ")
        self.speak("Done Sir")

    #voicebox().greeting
    def greeting(self):    
        greeting_values = ['Hello Sir', 'Always at your service sir', 'Yes Sir']
        command_voi=''
        g = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                command = g.listen(source, timeout=2, phrase_time_limit=5)
                
                command_voi = g.recognize_google(command, language='en-in')
                if 'wake up' in command_voi or 'are you there' in command_voi or 'jarvis help' in command_voi:
                    greet = random.choice(greeting_values)
                    voicebox().speak(greet)
                elif 'close' in command_voi:
                    self.speak("see you later sir")
                    exit()
                else:
                    voicebox().greeting()
        except Exception:
            voicebox().greeting()
    #ear- hearing system

    def takeCommand(self):
        try:
            r = sr.Recognizer()##################################################################
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source,timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Sir Said: {query}\n")


        except Exception as e:   
            print("Say that again please...")  
            print (e)
            return "None"
        return query

def calculate(numO,numS,operator):
    if operator =="x" or operator=="into":
        operator = "*"
    elif operator=="over":
        operator="/"
    strAns = str(numO)+operator+str(numS)
    return eval(strAns)


class brain:
    def execute(self,value):
        self.value = value
        if 'hello' in value or 'hi' in value:
            voicebox().speak("long time no see, sir")
            time.sleep(3)
            
            
        elif 'open telegram i want to talk to her' in value:
            os.startfile("C:\\Users\\Admin\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
            voicebox().speak("sure sir")
            
        elif 'by for now' in value or 'bye for now' in value:
            voicebox().speak("should i ask her out for you sir.")
            voicebox().greeting()
            
        elif 'who are you' in value or 'tell me about yourself' in value:
            voicebox().speak("My name is Jarvis. and I am a AI program, Created by Vipul Dixit.")

        elif 'what can you do' in  value:
            voicebox().speak(" I can do almost every thing, that you want. You can Start by, saying Hello")

        elif 'wikipedia' in value:
            voicebox().speak('Searching Wikipedia...')
            value = value.replace("wikipedia", "")
            results = wikipedia.summary(value, sentences=2)
            voicebox().speak("According to Wikipedia")
            print(results)
            voicebox().speak(results)

        elif 'open youtube' in value:
            webbrowser.open("https://www.youtube.com")
            voicebox().speak("opening Youtube")

        elif 'open google' in value:
            webbrowser.open("https://www.google.com")
            voicebox().speak("opening google")

        elif 'open stackoverflow' in value:
            webbrowser.open("stackoverflow.com")
            voicebox().speak("opening website")

        elif 'play music' in value:
            music_dir = 'A:\\songs\\Bollywood'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            voicebox().greeting()
        elif 'how are you' in value:
            voicebox().speak("Absolutly Fine")

        elif 'time' in value or 'the time' in value:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            voicebox().speak(f"Sir, the time is {strTime}")

        elif 'open code' in value:
            codePath = "P:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'google for' in value:
            search_item = value.split()
            filter_search = search_item[2:]
            join_search = " ".join(filter_search)
            voicebox().speak("searching google")
            webbrowser.open("https://www.google.com/search?q=" + join_search) 
            
        elif 'search in youtube' in value:
            searchyt_item = value.split() 
            filter_searchyt = searchyt_item[4:]
            url =  " ".join(filter_searchyt)
            voicebox().speak("searching in youtube for" + url)
            webbrowser.open("https://www.youtube.com/results?search_query="+url+"&page=&utm_source=opensearch")
            
        elif 'open Whatsapp' in value:
            WhatsappPath = "whatsapp"
            os.startfile(WhatsappPath)
            voicebox().speak("opening Whatsapp")

        elif 'see you later' in value:
            voicebox().speak("Bye Sir!")
            voicebox().greeting()
        

        elif 'bye jarvis' in value or 'by jarvis' in value:
            voicebox().speak("have a good day sir")
            exit()

        elif 'open website' in value:
            voicebox().speak("whats its name Sir")
            website_name = voicebox().takeCommand()
            website_name = f"https://www.{website_name}.com/"
            voicebox().speak("Opening" + website_name)
            webbrowser.open(website_name)

        elif 'close chrome' in value:   
            browser = "brave.exe"
            voicebox().speak("closing")
            os.system("taskkill /f /im "+browser)
                

        #elif 'shutdown pc' in value:
         #   voicebox().speak("Initializing Shutdown process. Bye Sir")
          #  os.system("shutdown /s /t 5")
           # exit()

        elif 'calculate' in value or 'evaluate' in value:
            if len(value)>9:
                ans = []
                op = []
                value = value.split(" ")
                for item in value[1:]:
                    if item in ["+","-","x","/","into","over"]:
                        op.append(item)
                    else:
                        ans.append(item)
                        if len(ans)==2 and len(op)==1:
                            b = ans.pop()
                            a = ans.pop()
                            oper = op.pop()
                            ans.append(calculate(a,b,oper))
                print(ans[0])
                voicebox().speak(ans[0])

        elif "train" in value or "lets learn" in value:
            print("Entering trainnnig mode")
            voicebox().speak("Entering Training Mode")
        else:
            pass


