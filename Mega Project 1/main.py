


import os
import webbrowser
import datetime
import requests
import speech_recognition as sr
import pyttsx3
import musicLibrary

from dotenv import load_dotenv
from openai import OpenAI


# =========================================================
# LOAD API KEYS FROM .env
# =========================================================

load_dotenv()

# API KEYS YAHAN DIRECTLY MAT DALO
# Keys .env file mein rakho

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# =========================================================
# INITIALIZATION
# =========================================================

recognizer = sr.Recognizer()
engine = pyttsx3.init()

client = None

if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)


# =========================================================
# SPEAK
# =========================================================

def speak(text):

    print("Jarvis:", text)

    try:
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Speech Error:", e)


# =========================================================
# TAKE COMMAND
# =========================================================

def take_command():

    try:

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("Listening...")

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            return command

    except sr.WaitTimeoutError:

        print("No speech detected.")
        return input("Type your command: ")

    except sr.UnknownValueError:

        print("Could not understand audio.")
        return input("Type your command: ")

    except Exception as e:

        print("Microphone Error:", e)
        return input("Type your command: ")


# =========================================================
# AI FUNCTION
# =========================================================

def ask_ai(question):

    if not client:

        speak(
            "OpenAI is not configured. "
            "Please add your OpenAI API key in the .env file."
        )

        return

    try:

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful AI voice assistant. "
                        "Give short and clear answers suitable for speaking."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],

            max_tokens=300
        )

        answer = response.choices[0].message.content

        if answer:

            speak(answer)

    except Exception as e:

        print("OpenAI Error:", e)

        speak(
            "Sorry, I could not connect to the AI service."
        )


# =========================================================
# NEWS FUNCTION
# =========================================================

def get_news():

    if not NEWS_API_KEY:

        speak(
            "News API is not configured. "
            "Please add your News API key in the .env file."
        )

        return

    speak(
        "Getting the latest news."
    )

    try:

        url = (
            "https://newsapi.org/v2/everything"
            "?q=India"
            "&language=en"
            "&sortBy=publishedAt"
            "&pageSize=5"
            f"&apiKey={NEWS_API_KEY}"
        )

        response = requests.get(
            url,
            timeout=10
        )

        print(
            "News API Status:",
            response.status_code
        )

        if response.status_code == 200:

            data = response.json()

            print(
                "API Status:",
                data.get("status")
            )

            print(
                "Total Results:",
                data.get("totalResults")
            )

            articles = data.get(
                "articles",
                []
            )

            if not articles:

                speak(
                    "Sorry, no latest news was found."
                )

                return

            speak(
                "Here are the latest news headlines."
            )

            for article in articles[:5]:

                title = article.get("title")

                if title:

                    print(
                        "News:",
                        title
                    )

                    speak(title)

        else:

            print(
                "News API Response:"
            )

            print(
                response.text
            )

            speak(
                "Sorry, I could not fetch the news."
            )

    except requests.exceptions.ConnectionError:

        speak(
            "Please check your internet connection."
        )

    except requests.exceptions.Timeout:

        speak(
            "The news service is taking too long to respond."
        )

    except Exception as e:

        print(
            "News Error:",
            e
        )

        speak(
            "There was an error while getting the news."
        )


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    speak(
        "Initializing Jarvis."
    )

    speak(
        "How can I help you?"
    )

    while True:

        command = take_command()

        if not command:
            continue

        print(
            "You said:",
            command
        )

        command_lower = command.lower().strip()


        # =================================================
        # GOOGLE
        # =================================================

        if "open google" in command_lower:

            speak(
                "Opening Google."
            )

            webbrowser.open(
                "https://www.google.com"
            )


        # =================================================
        # YOUTUBE
        # =================================================

        elif "open youtube" in command_lower:

            speak(
                "Opening YouTube."
            )

            webbrowser.open(
                "https://www.youtube.com"
            )


        # =================================================
        # TWITTER
        # =================================================

        elif "open twitter" in command_lower:

            speak(
                "Opening Twitter."
            )

            webbrowser.open(
                "https://www.twitter.com"
            )


        # =================================================
        # LINKEDIN
        # =================================================

        elif "open linkedin" in command_lower:

            speak(
                "Opening LinkedIn."
            )

            webbrowser.open(
                "https://www.linkedin.com/"
            )


        # =================================================
        # HACKERRANK
        # =================================================

        elif "open hackerrank" in command_lower:

            speak(
                "Opening HackerRank."
            )

            webbrowser.open(
                "https://www.hackerrank.com/"
            )


        # =================================================
        # GMAIL
        # =================================================

        elif "open gmail" in command_lower:

            speak(
                "Opening Gmail."
            )

            webbrowser.open(
                "https://mail.google.com/"
            )


        # =================================================
        # GITHUB
        # =================================================

        elif "open github" in command_lower:

            speak(
                "Opening GitHub."
            )

            webbrowser.open(
                "https://github.com"
            )


        # =================================================
        # TIME
        # =================================================

        elif "time" in command_lower:

            now = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            speak(
                f"The time is {now}"
            )


        # =================================================
        # MUSIC
        # =================================================

        elif command_lower.startswith("play "):

            song = command_lower.split(
                "play ",
                1
            )[1].strip()

            if song in musicLibrary.music:

                speak(
                    f"Playing {song}."
                )

                webbrowser.open(
                    musicLibrary.music[song]
                )

            else:

                speak(
                    "Sorry, song not found."
                )


        # =================================================
        # NEWS
        # =================================================

        elif "news" in command_lower:

            get_news()


        # =================================================
        # AI
        # =================================================

        elif command_lower.startswith("jarvis"):

            question = command[
                len("jarvis"):
            ].strip()

            if question:

                ask_ai(question)

            else:

                speak(
                    "Yes, how can I help you?"
                )


        # =================================================
        # ASK AI
        # =================================================

        elif command_lower.startswith("ask ai"):

            question = command[
                len("ask ai"):
            ].strip()

            if question:

                ask_ai(question)

            else:

                speak(
                    "What would you like me to answer?"
                )


        # =================================================
        # GENERAL QUESTIONS
        # =================================================

        elif any(
            word in command_lower
            for word in [
                "what is",
                "who is",
                "why is",
                "how do",
                "how can",
                "explain",
                "tell me about",
                "define"
            ]
        ):

            ask_ai(command)


        # =================================================
        # EXIT
        # =================================================

        elif (
            "exit" in command_lower
            or "quit" in command_lower
            or "goodbye" in command_lower
            or "stop jarvis" in command_lower
        ):

            speak(
                "Goodbye. Have a great day!"
            )

            break


        # =================================================
        # UNKNOWN COMMAND
        # =================================================

        else:

            speak(
                "I don't understand that command. "
                "You can ask me anything by saying Jarvis."
            )
