import pyttsx3


def speak(text):

    try:

        print("Jarvis:", text)

        # Use SAPI5 explicitly (Windows)
        engine = pyttsx3.init(driverName='sapi5')

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[1].id)

        engine.setProperty('rate', 160)

        engine.setProperty('volume', 1.0)

        engine.say(str(text))

        engine.runAndWait()

        engine.stop()

    except Exception as e:

        print("Speak Error:", e)