import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None

    return query

# Function to handle user commands
def handle_command(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        query = command.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
    elif 'play music' in command:
        music_dir = 'd:/Music'  # Replace with your music directory
        songs = os.listdir(music_dir)
        random.shuffle(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif('exit' in command and len(command)==4):
        speak("Goodbye!")
        exit()

# Main program loop
def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if command:
            handle_command(command.lower())

if __name__ == "__main__":
    main()
