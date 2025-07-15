import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech
import datetime  # For getting the current time
import wikipedia  # For Wikipedia searches
import webbrowser  # For opening web pages
import os  # For interacting with the operating system
import random  # For random selection
import platform  # For detecting the operating system

# Initialize text-to-speech engine
<<<<<<< HEAD
def initialize_engine():
    # Determine the operating system and select the appropriate TTS driver
    system_platform = platform.system()
    try:
        if system_platform == "Windows":
            engine = pyttsx3.init('sapi5')  # Use 'sapi5' for Windows
        else:
            engine = pyttsx3.init('espeak')  # Use 'espeak' for Linux/macOS
        
        # Set voice properties
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Select the first available voice
        return engine
    except Exception as e:
        print(f"Error initializing TTS engine: {e}")
        exit("Text-to-speech initialization failed. Ensure dependencies are installed.")

engine = initialize_engine()
=======
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
>>>>>>> 0dbf354 (	modified:   main.py)

# Function to speak the given text
def speak(text):
    try:
        # Use the TTS engine to speak the provided text
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking text: {e}")

# Function to listen to user input
def listen():
    # Initialize the speech recognizer
    r = sr.Recognizer()
    try:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1  # Adjust silence threshold
            audio = r.listen(source)  # Listen for audio input

        # Recognize the audio input using Google's speech recognition
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User: {query}\n")
        return query
    except sr.UnknownValueError:
        # Handle cases where the audio is not recognized
        print("Sorry, I didn't catch that. Can you please repeat?")
        speak("Sorry, I didn't catch that. Can you please repeat?")
    except sr.RequestError as e:
        # Handle errors with the speech recognition service
        print(f"Speech recognition service error: {e}")
        speak("There seems to be an issue with the speech recognition service.")
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
    return None

# Function to handle user commands
def handle_command(command):
<<<<<<< HEAD
    try:
        if 'wikipedia' in command:
            # Search Wikipedia for the query and return a summary
            speak('Searching Wikipedia...')
            query = command.replace('wikipedia', '').strip()
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in command:
            # Open YouTube in the web browser
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in command:
            # Open Google in the web browser
            webbrowser.open("https://www.google.com")
        elif 'play music' in command:
            # Play a random music file from the specified directory
            music_dir = 'd:/Music'  # Replace with your music directory
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    random.shuffle(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No music files found in the directory.")
            else:
                speak("Music directory not found. Please check the path.")
        elif 'the time' in command:
            # Tell the current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif 'exit' in command and len(command) == 4:
            # Exit the program when the user says "exit"
            speak("Goodbye!")
            exit()
        else:
            # Handle unrecognized commands
            speak("I'm sorry, I didn't understand that command.")
    except Exception as e:
        # Handle errors during command processing
        print(f"Error handling command: {e}")
        speak("An error occurred while processing your command.")
=======
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
    # elif 'play music' in command:
    #     music_dir = 'd:/Music'  # Replace with your music directory
    #     songs = os.listdir(music_dir)
    #     random.shuffle(songs)
    #     os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif('exit' in command and len(command)==4):
        speak("Goodbye!")
        exit()
>>>>>>> 0dbf354 (	modified:   main.py)

# Main program loop
def main():
    # Greet the user at the start of the program
    speak("Hello! How can I assist you today?")
    while True:
        # Continuously listen for and process commands
        command = listen()
        if command:
            handle_command(command.lower())

# Run the program
if __name__ == "__main__":
    main()
