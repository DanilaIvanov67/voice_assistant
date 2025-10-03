import pyaudio
import speech_recognition as sr
import os
import time
import pyttsx3
import webbrowser
import random
from tqdm import tqdm
r = sr.Recognizer()
voice = pyttsx3.init()
greetings=["И тебе привет","Здарова,задолбал","Приветствую","Доброго времени суток"]
pokedova=["Пока","До свидания","Всего доброго","адьос"]
zadalbalovka=0
voice.say("Здравствуйте, я ваш голосовой помошник")
voice.runAndWait()
while True:
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали:",speech)

        if "привет" in speech or "здравствуй" in speech:
            zadalbalovka=zadalbalovka+1
            if zadalbalovka==1:
                voice.say(random.choice(greetings))
                voice.runAndWait()
            elif zadalbalovka ==2:
                voice.say("Мы уже здаровались")

        elif  "пока" in speech or "до свидания" in speech :
            voice.say(random.choice(pokedova))
            voice.runAndWait()
            break
        elif "minecraft" in speech or "mine" in speech :
            voice.say("Запускаю майн")
            voice.runAndWait()
            os.startfile("C:/Users/Avengers/AppData/Roaming/.minecraft/TLauncher.exe")
        elif speech=="включи youtube":
            voice.say("Вы имели в виду,удалить system32? ")
            voice.runAndWait()
            for i in tqdm(range(100), desc="Удаление system32", unit="%", ncols=100):
                time.sleep(0.1)
            break
        elif "погода" in speech or "погоду" in speech:
            webbrowser.open_new("https://www.gismeteo.ru/weather-samara-4618/")
        else:
            voice.say("Я ничего не понимаю. Повторите пожалуйста")
            voice.runAndWait()
    except:
        print("Ошибка распознования")
