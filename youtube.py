from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import speech_recognition as sr
import pyttsx3 as p

# Initialize speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening for video query...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        speak("Could not request results from Google Speech Recognition service.")
        return ""

# Selenium class to handle YouTube
class music():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("start-maximized")

        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)

        # Wait for the video to be present
        wait = WebDriverWait(self.driver, 30)
        video = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]')))
        video.click()

        # Allow the video to play for a while
        time.sleep(120)

# Main function to handle video request
def play_video():
    speak("You want me to play which video?")
    video_query = listen_for_command()  # Get the video query from the user

    if video_query:
        speak(f"Playing {video_query} on YouTube.")
        assist = music()
        assist.play(video_query)
    else:
        speak("I didn't catch the video name, please try again.")

if __name__ == "__main__":
    play_video()
