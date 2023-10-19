import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time
import random

# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""

# Function to tell the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Function to search the web
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}.")

# Function to set a reminder
def set_reminder(reminder, minutes):
    speak(f"I will remind you to {reminder} in {minutes} minutes.")
    time.sleep(minutes * 60)
    speak(f"Reminder: {reminder}")

# Function to tell a random joke
def tell_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I used to play piano by ear, but now I use my hands.",
        "Parallel lines have so much in common. It's a shame they'll never meet."
    ]
    joke = random.choice(jokes)
    speak(joke)

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if "time" in command:
            tell_time()
        elif "search" in command:
            query = command.replace("search", "")
            search_web(query)
        elif "remind me to" in command:
            reminder = command.replace("remind me to", "")
            minutes = 1
            set_reminder(reminder, minutes)
        elif "joke" in command:
            tell_joke()
        elif "exit" in command:
            speak("Goodbye!")
            break
