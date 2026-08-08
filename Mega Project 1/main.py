
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import musicLibrary
import requests


# =========================
# INITIALIZATION
# =========================

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "7b0f8ddf0ac04232b26c2b56581671a6"


# =========================
# SPEAK
# =========================

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# =========================
# TAKE COMMAND
# =========================

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

        print("Microphone error:", e)
        return input("Type your command: ")


# =========================
# NEWS
# =========================

def get_news():

    speak("Getting the latest news.")

    try:

        url = (
            "https://newsapi.org/v2/everything"
            "?q=India"
            "&language=en"
            "&sortBy=publishedAt"
            "&pageSize=5"
            f"&apiKey={newsapi}"
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

            for article in articles:

                title = article.get("title")

                if title:

                    print(
                        "News:",
                        title
                    )

                    speak(title)

        else:

            print("API Response:")
            print(response.text)

            try:

                error_data = response.json()

                print(
                    "API Error:",
                    error_data.get("message")
                )

            except Exception:
                pass

            speak(
                "Sorry, I could not fetch the news."
            )

    except requests.exceptions.ConnectionError:

        print(
            "Internet connection error."
        )

        speak(
            "Please check your internet connection."
        )

    except requests.exceptions.Timeout:

        print(
            "News request timed out."
        )

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


# =========================
# MAIN PROGRAM
# =========================

if __name__ == "__main__":

    speak(
        "Initializing Jarvis."
    )

    while True:

        command = take_command()

        if not command:
            continue

        print(
            "You said:",
            command
        )

        command_lower = command.lower()


        # =========================
        # GOOGLE
        # =========================

        if "open google" in command_lower:

            speak(
                "Opening Google"
            )

            webbrowser.open(
                "https://www.google.com"
            )


        # =========================
        # YOUTUBE
        # =========================

        elif "open youtube" in command_lower:

            speak(
                "Opening YouTube"
            )

            webbrowser.open(
                "https://www.youtube.com"
            )


        # =========================
        # TWITTER
        # =========================

        elif "open twitter" in command_lower:

            speak(
                "Opening Twitter"
            )

            webbrowser.open(
                "https://www.twitter.com"
            )


        # =========================
        # LINKEDIN
        # =========================

        elif "open linkedin" in command_lower:

            speak(
                "Opening LinkedIn"
            )

            webbrowser.open(
                "https://www.linkedin.com/"
            )


        # =========================
        # HACKERRANK
        # =========================

        elif "open hackerrank" in command_lower:

            speak(
                "Opening HackerRank"
            )

            webbrowser.open(
                "https://www.hackerrank.com/"
            )


        # =========================
        # GMAIL
        # =========================

        elif "open gmail" in command_lower:

            speak(
                "Opening Gmail"
            )

            webbrowser.open(
                "https://mail.google.com/"
            )


        # =========================
        # GITHUB
        # =========================

        elif "open github" in command_lower:

            speak(
                "Opening GitHub"
            )

            webbrowser.open(
                "https://github.com"
            )


        # =========================
        # TIME
        # =========================

        elif "time" in command_lower:

            now = datetime.datetime.now().strftime(
                "%H:%M"
            )

            speak(
                f"The time is {now}"
            )


        # =========================
        # MUSIC
        # =========================

        elif command_lower.startswith("play "):

            song = command_lower.split(
                "play ",
                1
            )[1].strip()

            if song in musicLibrary.music:

                speak(
                    f"Playing {song}"
                )

                webbrowser.open(
                    musicLibrary.music[song]
                )

            else:

                speak(
                    "Sorry, song not found."
                )


        # =========================
        # NEWS
        # =========================

        elif "news" in command_lower:

            get_news()


        # =========================
        # EXIT
        # =========================

        elif (
            "exit" in command_lower
            or "quit" in command_lower
            or "goodbye" in command_lower
        ):

            speak(
                "Goodbye!"
            )

            break


        # =========================
        # UNKNOWN COMMAND
        # =========================

        else:

            speak(
                "Sorry, I didn't understand that."
            )

