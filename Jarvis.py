import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import pyaudio #pip install PyAudio
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install PyAutoGUI
import psutil
import pyjokes
import selenium
import wolframalpha
from googletrans import Translator
from newsapi import NewsApiClient 
from time import sleep
import unsplash_search
import requests
import wget
import subprocess
import ctypes
import getpass
import pywhatkit
import winsound
import threading
from pywikihow import search_wikihow #pip install pywikihow
from faceRecognition_master import livefacerecognizer  #pip install opencv-contrib-python
from PyQt5 import QtWidgets,QtCore,QtGui, sip
from PyQt5.QtCore import QTimer,QTime, QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_MainWindow
import sys


SPI_SETDESKWALLPAPER = 20 



engine = pyttsx3.init()
client =wolframalpha.Client('T9J9WV-4W2LYW8QJ3')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query =r.recognize_google(audio, language ='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("")
        return "None"

    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme(uname):
    speak("Welcome "+uname+" sir I am roma")

    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    elif hour >=18 and hour <23:
        speak("Good Evening")
    else:
        speak("Good Evening")
    
    

    speak("How can I help You")

def screenshot():

    img = pyautogui.screenshot()
    date =datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
    path="C:\\Jarvis\\Screenshot\\ScreenShot_"+date+".png"
    filename = os.listdir("C:\\")
    if 'Jarvis' in filename:
        files= os.listdir("C:\Jarvis")
        if 'Screenshot' in files:
            img.save(path)
        else:
            os.mkdir("C:\\Jarvis\\Screenshot")
            img.save(path)
    else :
        os.makedirs("C:\\Jarvis\\Screenshot")
        img.save(path) 
def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at' +usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def Translate():

	speak("what I should Translate??")
	sentence = takeCommand().lower()
	trans = Translator()
	trans_sen = trans.translate(sentence,src='en',dest='mr')
	print(trans_sen.text)
	speak(trans_sen.text)
    

def news():
    newsapi = NewsApiClient(api_key='57aead5647ab48e0886c10dabe6196a7')
    data = newsapi.get_top_headlines(q='india',country='in',
                                      language='en',
                                      page_size=3)
    at = data['articles']

    for x,y in enumerate(at):
        print(f'{x} {y["description"]}')
        speak(f'{x} {y["description"]}')
        
    speak("that's it for now i'll updating you in some time ")

def get_wallpaper(path):
	access_key = 'A06xFEuSQ2KI-7K86B31yKXGWKRd_uQtHXEWs9adfFs' 
	url = 'https://api.unsplash.com/photos/random?client_id=' + access_key
	params = {
		'query': 'HD wallpapers',
		'orientation': 'landscape'
	}

	response = requests.get(url, params=params).json()
	image_source = response['urls']['full']
	image = wget.download(image_source, path) 
	return image






def change_wallpaper(path):
    wallpaper = get_wallpaper(path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)





class thread(threading.Thread):
    def __init__(self, thread_hr, thread_min):
        threading.Thread.__init__(self)
        self.thread_hr = thread_hr
        self.thread_min = thread_min
 
        # helper function to execute the threads
    def run(self):
        

        while True:
            if self.thread_hr==datetime.datetime.now().hour:
                if self.thread_min==datetime.datetime.now().minute:
                    
                    print("Alarm in running")
                    winsound.PlaySound("abc", winsound.SND_LOOP)
                elif self.thread_min < datetime.datetime.now().minute:
                    
                    break
       





class MainTread(QThread):
    def __init__(self):
        super(MainTread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing....")
            query =r.recognize_google(audio, language ='en-in')
            print(query)

        except Exception as e:
            print(e)
            speak("Please say that again....")
            return "None"
        return query


    def TaskExecution(self):
        count, name = livefacerecognizer.checkUser()
        if count != 0:
            wishme(name)
            
            while True:
                self.query=self.takeCommand().lower()
                if 'roma' in self.query:
                    self.query = self.query.replace('roma','')
                    if 'time' in self.query:
                        time()
                    elif 'date' in self.query:
                        date()
                    elif 'about yourself' in self.query:
                        speak('"Roma is an artificial intelligence–powered virtual assistant developed by us.""Programming language use to develope roma is python.""The assistant uses voice queries and a natural-language user interface to answer questions, make recommendations, and perform actions by delegating requests to a set of Internet services. "')
                    elif 'wikipedia' in self.query: #wikipedia sachin tendulkar
                        try:
                            speak('searching....')
                            self.query=self.query.replace("wikipedia","")
                            result =wikipedia.summary(self.query , sentences=2)
                            print(result)
                            speak(result)
                        except:
                            speak("Unable to find query Please try again")
                    elif 'search website in chrome' in self.query: 
                        speak('what you want to search')
                        chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                        search = takeCommand().lower()
                        wb.get(chromepath).open_new_tab(search+'.com')
                    elif 'open youtube' in self.query:
                        wb.open("youtube.com")
                    elif 'play' in self.query:
                        self.query=self.query.replace("play","")
                        speak('playing ' + self.query)
                        pywhatkit.playonyt(self.query)
                    elif 'remember that' in self.query:
                        speak("what should i remember?")
                        data = takeCommand()
                        speak("you said me to remember that" +data)
                        path="C:/Jarvis/Data/"
                        filename = os.listdir("C:\\")
                        
                        if 'Jarvis' in filename:
                            files=  os.listdir("C:\\Jarvis")
                            if "Data" in files:
                                remember =open('C:/Jarvis/Data/data.txt','w')
                                remember.write(data)
                            else:
                                os.mkdir("C:\\Jarvis\\Data")
                                remember =open('C:/Jarvis/Data/data.txt','w')
                                remember.write(data)
                        else :
                            os.makedirs("C:\\Jarvis\\Data")   
                            remember =open('C:/Jarvis/Data/data.txt','w')
                            remember.write(data)
                        remember.close()
                    elif 'forget anything' in self.query:
                        remember =open('C:/Jarvis/Data/data.txt', 'r')
                        speak("you said me remember that" +remember.read())
                    elif 'screenshot' in self.query:
                        screenshot()
                        speak("done!")
                    elif 'cpu' in self.query:
                        cpu()
                    elif 'joke' in self.query:
                        jokes()
                    elif 'whatsapp' in self.query:
                        wapath = "C:\\Users\\rupes\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                        os.startfile(wapath)
                    elif 'telegram' in self.query:
                        tgpath = "C:\\Users\\rupes\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                        os.startfile(tgpath)
                    elif 'google' in self.query: #google square root of 4
                        print('searching....')
                        speak('searching....')
                        try:
                            try:
                                self.query=self.query.replace("google","")
                                res=client.query(self.query)
                                results=next(res.results).text
                                print(results)
                                speak(results)
                            except:
                                results = wikipedia.summary(self.query, sentences=2)
                                print(results)
                                speak(results)
                        except:
                            wb.open('www.google.com')
                    elif 'translate' in self.query: #translate
                        Translate()
                    elif 'news' in self.query:
                        news()
                    elif 'change wallpaper' in self.query:
                        path="C:/Jarvis/Wallpaper/wallpaper_"+datetime.datetime.now().strftime("%m%d%Y_%H%M%S")+".jpg"
                        filename = os.listdir("C:\\")
                        
                        if 'Jarvis' in filename:
                            files=  os.listdir("C:\\Jarvis")
                            if "Wallpaper" in files:
                                change_wallpaper(path)
                            else:
                                os.mkdir("C:\\Jarvis\\Wallpaper")
                                change_wallpaper(path)
                        else :
                            os.makedirs("C:\\Jarvis\\Wallpaper")
                            change_wallpaper(path)     
                        
                        speak('Successfully change.')
                    elif 'thank you' in self.query:
                        speak("'Welcome sir.''Its my pleasure to serve you.'")
                    elif 'break' in self.query:
                        speak("going offline for while")
                        sleep(60)
                    elif 'offline' in self.query:
                        sys.exit()    
                    elif 'close' in self.query:
                        os.system("taskkill /F /IM WhatsApp.exe")
                    elif "alarm" in self.query:#set alarm #
                        speak("Tell Time")
                        try:
                            tt = takeCommand()
                            tt =tt.replace("set alarm to","")
                            tt=tt.replace(".","")
                            tt=tt.upper()

                            altime= str(datetime.datetime.now().strptime(tt,"%I:%M %p"))
                            altime =altime[11:-3]
                            print(altime)
                            Horeal =altime[:2]
                            Horeal = int(Horeal)
                            Mireal = altime[3:5]
                            Mireal=int(Mireal)
                            print(f"Done, {tt}")    
                            speak(f"Done, {tt}")
                            thread1 = thread(Horeal, Mireal)
                            thread1.start()
                        

                            #alarm(tt)
                        except Exception as e:
                            speak("Not able to set alarm please tell time in right format For example 4 02 PM ")
                    elif "how to" in self.query:#how to
                        speak("Search mode activates")
                        while True:
                            speak("What you want to know?")
                            how =takeCommand()
                            try:
                                if "close" in how:
                                    speak("Mode deactivate!")
                                    break
                                else:
                                    max_results =1
                                    how_to =search_wikihow(how,max_results)
                                    assert len(how_to)==1
                                    how_to[0].print()
                                    speak(how_to[0].summary)
                            except Exception as e:
                                speak("Sorry,Unable to find.")
                    elif "volume up" in self.query:
                        pyautogui.press("volumeup")
                    elif "volume down" in self.query:
                        pyautogui.press("volumedown")
                    elif "mute" in self.query:
                        pyautogui.press("volumemute")
                    elif "unmute" in self.query:
                        pyautogui.press("volumemute")
                    elif "location" in self.query:
                        speak("Let me check")
                        try:
                            ipAdd= requests.get('https://api.ipify.org').text
                            print(ipAdd)
                            url = "https://get.geojs.io/v1/ip/geo/" +ipAdd+'.json'
                            geo_request= requests.get(url)
                            geo_data =geo_request.json()
                            city= geo_data['city']
                            country = geo_data['country']
                            print(city,country)
                            speak(f"location{city}in{country}")
                        except Exception as e:
                            speak("sorry")
                            pass
                    elif "camera" in self.query:
                        subprocess.run('start microsoft.windows.camera:', shell=True)
                    elif "tab" in self.query:
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        sleep(1)
                        pyautogui.keyUp("alt")
                    elif 'logout' in self.query:
                        os.system("shutdown -l")
                    elif 'restart' in self.query:
                        os.system("shutdown /r /t 1")
                    elif 'shutdown' in self.query:

                        os.system("shutdown /s /t 1")
                    elif 'check user' in self.query:
                        count, name = livefacerecognizer.checkUser()
                        if count != 0:
                            speak("Hello ")
                            speak(name)
                        if count == 0:
                            speak("Unable to identify user")      
                    elif 'who am i' in self.query:
                        livefacerecognizer.live()
                        speak("identifying user")
                        speak("hello "+name)          
        else:
            speak("Unauthorized user detected please contact admin")

startExecution=MainTread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("E:/Jarvis/mini project/new.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())