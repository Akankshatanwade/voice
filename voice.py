import speech_recognition as sr
from datetime import datetime
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def basic_voice_assistant():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "hello" in command:
            say("Hello! How can I help you?")
        elif "time" in command:
            current_time = datetime.now().strftime("%H:%M:%S")
            say(f"The current time is {current_time}")
        elif "date" in command:
            current_date = datetime.now().strftime("%Y-%m-%d")
            say(f"Today's date is {current_date}")
        elif "search" in command:
            query = command.replace("search", "").strip()
            say(f"Searching the web for {query}...")
            # Implement web search functionality here

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    basic_voice_assistant()
