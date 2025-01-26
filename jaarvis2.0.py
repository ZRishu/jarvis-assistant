import pyttsx3 as pt  # Text-to-speech conversion
import datetime
import speech_recognition as sr
import smtplib
from secrets_1 import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
from newsapi import NewsApiClient
import os
import pyjokes
import time as tt
import string
import random
import nltk
from nltk.tokenize import word_tokenize

engine = pt.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("Hello human, I am Jarvis, your personal assistant.")
    elif voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello human, I am Friday, your personal assistant.")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is: " + Time)

def date():
    today = datetime.datetime.now()
    speak(f"The current date is {today.day} {today.month} {today.year}")

def greeting():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning, human.")
    elif 12 <= hour < 17:
        speak("Good afternoon, human.")
    elif 17 <= hour < 24:
        speak("Good evening, human.")
    else:
        speak("Good night, human.")

def wishme():
    speak("Welcome back, human!")
    time()
    date()
    greeting()
    speak("Jarvis at your service. Please tell me how may I help you?")

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        return query
    except Exception:
        speak("Please kindly repeat...")
        return "None"

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def send_whatsapp_msg(phone_no, message):
    wb.open(f'https://web.whatsapp.com/send?phone={phone_no}&text={message}')
    sleep(10)
    pyautogui.press('enter')

def search_google():
    speak("What do you want to search?")
    search = takeCommandMic()
    wb.open(f'https://www.google.com/search?q={search}')

def news():
    newsapi = NewsApiClient(api_key='6a875544e554815878d4e938968bf19')
    speak("What do you want to know about?")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic, language='en', country='in', page_size=5)
    for i, article in enumerate(data['articles']):
        speak(f'{i + 1}. {article["description"]}')
    speak("These are the top headlines for today.")

def text2speech():
    speak("What do you want me to speak?")
    text = takeCommandMic()
    speak(text)

def screenshot():
    name_img = f'screenshot_{tt.time()}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def password_generator():
    chars = string.ascii_letters + string.digits + string.punctuation
    newpass = ''.join(random.choice(chars) for _ in range(8))
    speak(newpass)

def flip():
    speak("Flipping a coin.")
    speak(random.choice(['Heads', 'Tails']))

def roll_a_die():
    speak("Rolling a die.")
    speak(random.choice(['1', '2', '3', '4', '5', '6']))

if __name__ == "__main__":
    wakeword = "jarvis"
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        if wakeword in query:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'email' in query:
                email_list = {'test email': 'xyz@gmail.com'}
                try:
                    speak("To whom do you want to send an email?")
                    name = takeCommandMic()
                    receiver = email_list.get(name, None)
                    if receiver:
                        speak("What is the subject?")
                        subject = takeCommandMic()
                        speak("What should I say?")
                        content = takeCommandMic()
                        sendEmail(receiver, subject, content)
                        speak("Email has been sent.")
                    else:
                        speak("I couldn't find the recipient.")
                except Exception:
                    speak("Unable to send email.")
            elif 'message' in query:
                user_contacts = {'Jarvis': '+919999657854'}
                try:
                    speak("To whom do you want to send a message?")
                    name = takeCommandMic()
                    phone_no = user_contacts.get(name, None)
                    if phone_no:
                        speak("What is the message?")
                        message = takeCommandMic()
                        send_whatsapp_msg(phone_no, message)
                        speak("Message has been sent.")
                    else:
                        speak("I couldn't find the contact.")
                except Exception:
                    speak("Unable to send message.")
            elif 'wikipedia' in query:
                query.remove('wikipedia')
                result = wikipedia.summary(' '.join(query), sentences=2)
                speak(result)
            elif 'search' in query:
                search_google()
            elif 'youtube' in query:
                speak("What do you want to search?")
                pywhatkit.playonyt(takeCommandMic())
            elif 'news' in query:
                news()
            elif 'read' in query:
                text2speech()
            elif 'password' in query:
                password_generator()
            elif 'flip' in query:
                flip()
            elif 'roll' in query:
                roll_a_die()
            elif 'offline' in query:
                quit()
