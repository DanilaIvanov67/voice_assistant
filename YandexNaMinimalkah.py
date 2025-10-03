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
predictions = ["Сегодня вас ждет неожиданная радость — возможно, небольшой, но приятный сюрприз, который поднимет настроение на весь день.",
"День идеально подходит для решения старых проблем. Смело беритесь за то, что долго откладывали, — вас ждет успех!",
"Вас ждет день важных встреч и решений. Будьте внимательны к деталям — именно в мелочах скрывается ключ к успеху.",
"Сегодняшний день преподаст вам небольшой, но важный урок. Прислушайтесь к своему внутреннему голосу, он подскажет верный путь.",
"Вас ждет приятная встреча или разговор с человеком, который подарит интересную идею или просто хорошее настроение.",
"Вселенная благоволит творческим начинаниям! Дерзайте, творите, выражайте себя — результат вас приятно удивит.",
"Фортуна улыбнется вам сегодня в самом неожиданном месте. Не бойтесь пробовать что-то новое!",
"Сегодня лучшая стратегия — не торопиться. Позвольте себе замедлиться, насладиться моментом, и вы найдете ответы на свои вопросы.",
"Вас ждет продуктивный день. Закончить дела вовремя не составит труда, главное — начать!",
"Сегодня судьба подаст вам знак. Будьте начеку: это может быть случайная фраза, знак на дороге или песня по радио."]
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
        elif "предсказание" in speech or "совет" in speech or "предсказания" in speech:
            voice.say("Предсказание на сегодня: " + random.choice(predictions))
            voice.runAndWait()
        else:
            voice.say("Я ничего не понимаю. Повторите пожалуйста")
            voice.runAndWait()
    except:
        print("Ошибка распознования")
