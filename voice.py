import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow  # Import the infow class
from youtube import music  # Import the music class

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

# Greeting
speak("Hello ma'am, I'm your voice assistant. How are you?")

try:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(f"You said: {text}")

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
    speak("Sorry, I didn't catch that.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
    speak("Sorry, something went wrong with the recognition service.")

# Better condition check for specific words
if all(x in text.lower() for x in ["what", "about", "you"]):
    speak("I am also fine ma'am.")
    speak("What can I do for you?")

# Listen for further commands
try:
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening for command...")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(f"Command: {text2}")

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
    speak("Sorry, I didn't catch that.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
    speak("Sorry, something went wrong with the recognition service.")

# Process commands
if "information" in text2:
    speak("You need information related to which topic?")
    
    try:
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening for the topic...")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
            print(f"Searching for {infor} on Wikipedia")

        speak(f"Searching {infor} in Wikipedia.")
        assist = infow()
        assist.get_info(infor)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        speak("Sorry, I didn't catch the topic.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("Sorry, something went wrong with the recognition service.")

# Modified condition for "play video" command
elif "play" in text2 and "video" in text2:
    speak("You want me to play which video?")
    
    try:
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening for video query...")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
            print(f"Playing {vid} on YouTube")

        speak(f"Playing {vid} on YouTube.")
        assist = music()
        assist.play(vid)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        speak("Sorry, I didn't catch the video name.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("Sorry, something went wrong with the recognition service.")
