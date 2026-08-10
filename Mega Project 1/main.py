

import os
import webbrowser
import datetime

import speech_recognition as sr
import pyttsx3

from dotenv import load_dotenv
from openai import OpenAI


# Load .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Voice
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Groq
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
# MICROPHONE
# =========================================================

def take_command():

    try:

        microphones = sr.Microphone.list_microphone_names()

        mic_index = None

        for i, name in enumerate(microphones):

            if "Microphone Array 1" in name:
                mic_index = i
                break

        if mic_index is None:

            for i, name in enumerate(microphones):

                if "Microphone Array 2" in name:
                    mic_index = i
                    break

        with sr.Microphone(
            device_index=mic_index
        ) as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command

    except Exception as e:

        print("Microphone Error:", e)

        return ""


# =========================================================
# AI
# =========================================================

def ask_ai(question):

    if not client:

        return "Groq API is not configured."

    try:

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful AI assistant. "
                        "Give short and clear answers."
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

        return answer.strip()

    except Exception as e:

        print("Groq Error:", e)

        return "Sorry, I could not connect to Groq."


# =========================================================
# PROCESS COMMAND
# =========================================================

def process_command(command):

    if not command:
        return ""

    command_lower = command.lower().strip()


    # Exit

    if command_lower in [
        "exit",
        "quit",
        "goodbye",
        "stop jarvis"
    ]:

        response = "Goodbye!"

        speak(response)

        return "__EXIT__"


    # Google

    if "open google" in command_lower:

        response = "Opening Google."

        webbrowser.open(
            "https://www.google.com"
        )

        speak(response)

        return response


    # YouTube

    if "open youtube" in command_lower:

        response = "Opening YouTube."

        webbrowser.open(
            "https://www.youtube.com"
        )

        speak(response)

        return response


    # GitHub

    if "open github" in command_lower:

        response = "Opening GitHub."

        webbrowser.open(
            "https://github.com"
        )

        speak(response)

        return response


    # Time

    if "time" in command_lower:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        response = f"The time is {current_time}."

        speak(response)

        return response


    # Jarvis AI

    if command_lower.startswith("jarvis"):

        question = command[
            len("jarvis"):
        ].strip()

        if not question:

            response = "Yes, how can I help you?"

            speak(response)

            return response

        response = ask_ai(question)

        speak(response)

        return response


    # General AI question

    ai_words = [
        "what is",
        "who is",
        "why is",
        "how do",
        "how can",
        "explain",
        "tell me about",
        "define"
    ]

    if any(
        word in command_lower
        for word in ai_words
    ):

        response = ask_ai(command)

        speak(response)

        return response


    # Unknown command

    response = (
        "I don't understand that command. "
        "Try saying Jarvis followed by your question."
    )

    speak(response)

    return response


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    print("Jarvis backend loaded successfully.")

    print(
        "process_command available:",
        callable(process_command)
    )
