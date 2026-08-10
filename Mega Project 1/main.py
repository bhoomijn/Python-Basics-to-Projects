
import os
import webbrowser
import datetime
import requests
import speech_recognition as sr
import pyttsx3
import musicLibrary
import psutil

from dotenv import load_dotenv
from openai import OpenAI


# =========================================================
# LOAD ENVIRONMENT VARIABLES
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
        engine.say(str(text))
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
                duration=0.5
            )

            print("Listening...")

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            print("You said:", command)

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
# AI FUNCTION - GROQ
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
                        "You are a helpful desktop AI assistant. "
                        "Your name is Jarvis. "
                        "Give short, clear answers suitable for speaking."
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

            answer = answer.strip()

            speak(answer)

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
# NEWS FUNCTION
# =========================================================

def get_news():

    if not NEWS_API_KEY:

        message = (
            "News API is not configured. "
            "Please add your News API key in the .env file."
        )

        speak(message)
        return message

    try:

        speak("Getting the latest news.")

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

        if response.status_code != 200:

            print("News API Response:")
            print(response.text)

            message = "Sorry, I could not fetch the news."

            speak(message)

            return message

        data = response.json()

        articles = data.get(
            "articles",
            []
        )

        if not articles:

            message = "Sorry, no latest news was found."

            speak(message)

            return message

        speak("Here are the latest news headlines.")

        headlines = []

        for article in articles[:5]:

            title = article.get("title")

            if title:

                print("News:", title)

                headlines.append(title)

                speak(title)

        return " | ".join(headlines)

    except requests.exceptions.ConnectionError:

        message = "Please check your internet connection."

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
# WEATHER FUNCTION
# =========================================================

def get_weather():

    try:

        city = "Bhopal"

        url = (
            "https://wttr.in/"
            + city
            + "?format=Weather:+%C+|+Temperature:+%t+|+Humidity:+%h"
        )

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code == 200:

            weather = response.text.strip()

            print("Weather:", weather)

            message = (
                f"The weather in {city} is {weather}"
            )

            speak(message)

            return weather

        else:

            message = (
                "Sorry, I could not get the weather."
            )

            speak(message)

            return message

    except requests.exceptions.RequestException as e:

        print("Weather Error:", e)

        message = (
            "I could not connect to the weather service."
        )

        speak(message)

        return message

    except Exception as e:

        print("Weather Error:", e)

        message = "There was an error getting the weather."

        speak(message)

        return message


# =========================================================
# CALCULATOR
# =========================================================

def calculate(expression):

    try:

        expression = (
            expression
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("multiply", "*")
            .replace("multiplied by", "*")
            .replace("divide", "/")
            .replace("divided by", "/")
        )

        allowed = "0123456789+-*/().% "

        if not all(
            character in allowed
            for character in expression
        ):

            message = "I can only calculate basic mathematical expressions."

            speak(message)

            return message

        result = eval(
            expression,
            {
                "__builtins__": {}
            },
            {}
        )

        message = f"The answer is {result}"

        speak(message)

        return message

    except Exception:

        message = "Sorry, I could not calculate that."

        speak(message)

        return message


# =========================================================
# TIME
# =========================================================

def get_time():

    now = datetime.datetime.now().strftime(
        "%I:%M %p"
    )

    message = f"The time is {now}"

    speak(message)

    return message


# =========================================================
# DATE
# =========================================================

def get_date():

    today = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    message = f"Today is {today}"

    speak(message)

    return message


# =========================================================
# SYSTEM INFORMATION
# =========================================================

def get_system_info():

    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        battery = psutil.sensors_battery()

        if battery:
            battery_text = f"{battery.percent:.0f}%"
        else:
            battery_text = "Not available"

        info = (
            f"CPU usage is {cpu:.0f} percent. "
            f"RAM usage is {ram:.0f} percent. "
            f"Battery is {battery_text}."
        )

        print("System:", info)

        speak(info)

        return info

    except Exception as e:

        print("System Info Error:", e)

        message = "Sorry, I could not get the system information."

        speak(message)

        return message
    
# =========================================================
# OPEN WEBSITE
# =========================================================

def open_website(url, name):

    message = f"Opening {name}."

    speak(message)

    webbrowser.open(url)

    return message


# =========================================================
# PROCESS COMMAND
# =========================================================
# GUI IS FUNCTIONALLY CONNECTED TO THIS FUNCTION
# =========================================================

def process_command(command):

    if not command:

        return ""

    command = command.strip()

    command_lower = command.lower()

    print(
        "Processing:",
        command
    )


# =====================================================
# SYSTEM INFO
# =====================================================

    if (
    "system information" in command_lower
    or "system info" in command_lower
    or "cpu usage" in command_lower
    or "ram usage" in command_lower
    or "battery status" in command_lower
    or "computer status" in command_lower
):

        return get_system_info()

    # =====================================================
    # EXIT
    # =====================================================

    if (
        "exit" in command_lower
        or "quit" in command_lower
        or "goodbye" in command_lower
        or "stop jarvis" in command_lower
    ):

        message = "Goodbye. Have a great day!"

        speak(message)

        return "__EXIT__"


    # =====================================================
    # GOOGLE
    # =====================================================

    if "open google" in command_lower:

        return open_website(
            "https://www.google.com",
            "Google"
        )


    # =====================================================
    # YOUTUBE
    # =====================================================

    if "open youtube" in command_lower:

        return open_website(
            "https://www.youtube.com",
            "YouTube"
        )


    # =====================================================
    # TWITTER / X
    # =====================================================

    if (
        "open twitter" in command_lower
        or "open x" == command_lower
    ):

        return open_website(
            "https://twitter.com",
            "Twitter"
        )


    # =====================================================
    # LINKEDIN
    # =====================================================

    if "open linkedin" in command_lower:

        return open_website(
            "https://www.linkedin.com",
            "LinkedIn"
        )


    # =====================================================
    # HACKERRANK
    # =====================================================

    if "open hackerrank" in command_lower:

        return open_website(
            "https://www.hackerrank.com",
            "HackerRank"
        )


    # =====================================================
    # GMAIL
    # =====================================================

    if "open gmail" in command_lower:

        return open_website(
            "https://mail.google.com",
            "Gmail"
        )


    # =====================================================
    # GITHUB
    # =====================================================

    if "open github" in command_lower:

        return open_website(
            "https://github.com",
            "GitHub"
        )


    # =====================================================
    # TIME
    # =====================================================

    if (
        "what is the time" in command_lower
        or "what's the time" in command_lower
        or command_lower == "time"
        or "current time" in command_lower
    ):

        return get_time()


    # =====================================================
    # DATE
    # =====================================================

    if (
        "what is the date" in command_lower
        or "what's the date" in command_lower
        or command_lower == "date"
        or "today's date" in command_lower
    ):

        return get_date()


    # =====================================================
    # WEATHER
    # =====================================================

    if (
        "weather" in command_lower
        or "temperature" in command_lower
    ):

        return get_weather()


    # =====================================================
    # NEWS
    # =====================================================

    if (
        "news" in command_lower
        or "latest news" in command_lower
        or "today's news" in command_lower
    ):

        return get_news()


    # =====================================================
    # CALCULATOR
    # =====================================================

    if command_lower.startswith("calculate "):

        expression = command[
            len("calculate "):
        ].strip()

        return calculate(expression)


    # =====================================================
    # PLAY MUSIC
    # =====================================================

    if command_lower.startswith("play "):

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
    # WEB SEARCH
    # =====================================================

    if command_lower.startswith("search "):

        query = command[
            len("search "):
        ].strip()

        if query:

            message = f"Searching for {query}."

            speak(message)

            webbrowser.open(
                "https://www.google.com/search?q="
                + requests.utils.quote(query)
            )

            return message


    # =====================================================
    # JARVIS / AI
    # =====================================================

    if command_lower.startswith("jarvis"):

        question = command[
            len("jarvis"):
        ].strip()

        if question:

            return ask_ai(question)

        else:

            message = "Yes, how can I help you?"

            speak(message)

            return message


    # =====================================================
    # ASK AI
    # =====================================================

    if command_lower.startswith("ask ai"):

        question = command[
            len("ask ai"):
        ].strip()

        if question:

            return ask_ai(question)

        else:

            message = "What would you like me to answer?"

            speak(message)

            return message


    # =====================================================
    # GENERAL AI QUESTIONS
    # =====================================================

    ai_keywords = [
        "what is",
        "who is",
        "why is",
        "how do",
        "how can",
        "explain",
        "tell me about",
        "define",
        "what are",
        "what does"
    ]

    if any(
        keyword in command_lower
        for keyword in ai_keywords
    ):

        return ask_ai(command)


    # =====================================================
    # UNKNOWN COMMAND
    # =====================================================

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
            continue

        result = process_command(command)

        if result == "__EXIT__":

            break
