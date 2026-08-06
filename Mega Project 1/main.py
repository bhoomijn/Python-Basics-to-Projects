
 
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        print("Recognizing...")
        return recognizer.recognize_google(audio)
    except Exception:
        return input("Type your command: ")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        command = take_command()
        print("You said:", command)

        if "open google" in command.lower():
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "open youtube" in command.lower():
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open twitter" in command.lower():
            speak("Opening Twitter")
            webbrowser.open("https://www.twitter.com")
        elif "open linkedin" in command.lower():
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com/")
        elif "open gmail" in command.lower():
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com/")
        elif "open github" in command.lower():
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
        elif "time" in command.lower():
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        elif "exit" in command.lower():
            speak("Goodbye Bhoomi!")
            break
        else:
            speak("Sorry, I didn't understand that.")
