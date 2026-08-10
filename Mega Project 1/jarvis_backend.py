
import speech_recognition as sr
import pyttsx3
import os

from dotenv import load_dotenv
from groq import Groq

# =========================================================
# LOAD ENV
# =========================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# =========================================================
# INITIALIZE
# =========================================================

recognizer = sr.Recognizer()
engine = pyttsx3.init()

client = None

if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)


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
# LISTEN
# =========================================================

def listen():

    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command

    except sr.WaitTimeoutError:

        print("No speech detected.")
        return ""

    except sr.UnknownValueError:

        print("Could not understand.")
        return ""

    except Exception as e:

        print("Microphone Error:", e)
        return ""


# =========================================================
# ASK GROQ
# =========================================================

def ask_ai(question):

    if not client:

        return "Groq API is not configured."

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful voice assistant. "
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

        return answer or "I could not generate an answer."

    except Exception as e:

        print("Groq Error:", e)

        return "Sorry, I could not connect to the AI service."


# =========================================================
# PROCESS COMMAND
# =========================================================

def process_command(command):

    if not command:
        return "I didn't hear anything."

    answer = ask_ai(command)

    speak(answer)

    return answer

