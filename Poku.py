import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print (voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Poku sir. Please tell me how may I help you")


def takecommand():
    # It takes microphone input from user and covert it into a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wishme()
    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open linkedIN' in query:
            webbrowser.open('linkedin.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open wikipedia' in query:
            webbrowser.open('wikipedia.com')

        elif 'open google' in query:
            webbrowser.open('google.co.in')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Kumarz\\Desktop\\musicx'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir,the time is {strTime}")

        elif 'open code' in query:
            vPath = "C:\\Users\\Kumarz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vPath)

        elif 'open pycharm' in query:
            pPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.3\\bin\\pycharm64.exe"
            os.startfile(pPath)