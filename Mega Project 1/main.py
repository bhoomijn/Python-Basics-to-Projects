
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
# LOAD API KEYS
# =========================================================

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# =========================================================
# INITIALIZATION
# =========================================================

recognizer = sr.Recognizer()
engine = pyttsx3.init()

client = None

if GROQ_API_KEY:
    client = OpenAI(
        api_key=GROQ_API_KEY,
        base_url="https://api.groq.com/openai/v1"
    )


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
# TAKE VOICE COMMAND
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
        return ""

    except sr.UnknownValueError:

        print("Could not understand audio.")
        return ""

    except Exception as e:

        print("Microphone Error:", e)
        return ""


# =========================================================
# GROQ AI
# =========================================================

def ask_ai(question):

    if not client:

        message = (
            "Groq is not configured. "
            "Please add your Groq API key in the .env file."
        )

        speak(message)
        return message

    try:

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

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

            # IMPORTANT:
            # Send answer back to Pygame GUI
            return answer

        return "I could not generate an answer."

    except Exception as e:

        print("Groq Error:", e)

        message = (
            "Sorry, I could not connect to the AI service."
        )

        speak(message)

        return message


# =========================================================
# NEWS
# =========================================================

def get_news():

    if not NEWS_API_KEY:

        message = (
            "News API is not configured. "
            "Please add your News API key in the .env file."
        )

        speak(message)
        return message

    speak("Getting the latest news.")

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

            articles = data.get(
                "articles",
                []
            )

            if not articles:

                message = (
                    "Sorry, no latest news was found."
                )

                speak(message)
                return message

            headlines = []

            speak(
                "Here are the latest news headlines."
            )

            for article in articles[:5]:

                title = article.get("title")

                if title:

                    print("News:", title)

                    speak(title)

                    headlines.append(title)

            return "\n".join(headlines)

        else:

            print(
                "News API Response:",
                response.text
            )

            message = (
                "Sorry, I could not fetch the news."
            )

            speak(message)
            return message

    except requests.exceptions.ConnectionError:

        message = (
            "Please check your internet connection."
        )

        speak(message)
        return message

    except requests.exceptions.Timeout:

        message = (
            "The news service is taking too long to respond."
        )

        speak(message)
        return message

    except Exception as e:

        print("News Error:", e)

        message = (
            "There was an error while getting the news."
        )

        speak(message)
        return message


# =========================================================
# PROCESS COMMAND
# =========================================================

def process_command(command):

    if not command:
        return ""

    print("You said:", command)

    command_lower = command.lower().strip()


    # =====================================================
    # GOOGLE
    # =====================================================

    if "open google" in command_lower:

        message = "Opening Google."

        speak(message)

        webbrowser.open(
            "https://www.google.com"
        )

        return message


    # =====================================================
    # YOUTUBE
    # =====================================================

    elif "open youtube" in command_lower:

        message = "Opening YouTube."

        speak(message)

        webbrowser.open(
            "https://www.youtube.com"
        )

        return message


    # =====================================================
    # TWITTER
    # =====================================================

    elif "open twitter" in command_lower:

        message = "Opening Twitter."

        speak(message)

        webbrowser.open(
            "https://www.twitter.com"
        )

        return message


    # =====================================================
    # LINKEDIN
    # =====================================================

    elif "open linkedin" in command_lower:

        message = "Opening LinkedIn."

        speak(message)

        webbrowser.open(
            "https://www.linkedin.com/"
        )

        return message


    # =====================================================
    # HACKERRANK
    # =====================================================

    elif "open hackerrank" in command_lower:

        message = "Opening HackerRank."

        speak(message)

        webbrowser.open(
            "https://www.hackerrank.com/"
        )

        return message


    # =====================================================
    # GMAIL
    # =====================================================

    elif "open gmail" in command_lower:

        message = "Opening Gmail."

        speak(message)

        webbrowser.open(
            "https://mail.google.com/"
        )

        return message


    # =====================================================
    # GITHUB
    # =====================================================

    elif "open github" in command_lower:

        message = "Opening GitHub."

        speak(message)

        webbrowser.open(
            "https://github.com"
        )

        return message


    # =====================================================
    # TIME
    # =====================================================

    elif "time" in command_lower:

        now = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        message = f"The time is {now}"

        speak(message)

        return message


    # =====================================================
    # MUSIC
    # =====================================================

    elif command_lower.startswith("play "):

        song = command_lower.split(
            "play ",
            1
        )[1].strip()

        if song in musicLibrary.music:

            message = f"Playing {song}."

            speak(message)

            webbrowser.open(
                musicLibrary.music[song]
            )

            return message

        else:

            message = "Sorry, song not found."

            speak(message)

            return message


    # =====================================================
    # NEWS
    # =====================================================

    elif "news" in command_lower:

        return get_news()


    # =====================================================
    # JARVIS
    # =====================================================

    elif command_lower.startswith("jarvis"):

        question = command[
            len("jarvis"):
        ].strip()

        if question:

            return ask_ai(question)

        else:

            message = (
                "Yes, how can I help you?"
            )

            speak(message)

            return message


    # =====================================================
    # ASK AI
    # =====================================================

    elif command_lower.startswith("ask ai"):

        question = command[
            len("ask ai"):
        ].strip()

        if question:

            return ask_ai(question)

        else:

            message = (
                "What would you like me to answer?"
            )

            speak(message)

            return message


    # =====================================================
    # GENERAL AI QUESTIONS
    # =====================================================

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

        return ask_ai(command)


    # =====================================================
    # EXIT
    # =====================================================

    elif (
        "exit" in command_lower
        or "quit" in command_lower
        or "goodbye" in command_lower
        or "stop jarvis" in command_lower
    ):

        message = (
            "Goodbye. Have a great day!"
        )

        speak(message)

        return "__EXIT__"


    # =====================================================
    # UNKNOWN COMMAND
    # =====================================================

    else:

        message = (
            "I don't understand that command. "
            "You can ask me anything by saying Jarvis."
        )

        speak(message)

        return message


# =========================================================
# TERMINAL MODE
# =========================================================

if __name__ == "__main__":

    speak("Initializing Jarvis.")

    speak("How can I help you?")

    while True:

        command = take_command()

        if not command:

            command = input(
                "Type your command: "
            )

        if not command:
            continue

        result = process_command(command)

        if result == "__EXIT__":

            break
