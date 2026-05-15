import speech_recognition as sr

recognizer = sr.Recognizer()

def wait_for_wake_word():

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)

        print("Waiting for Jarvis...")

        while True:

            try:
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

                text = recognizer.recognize_google(audio).lower()

                print("Heard:", text)

                wake_words = [
                    "jar",
                    "jarvis",
                    "hey jarvis",
                    "hi jarvis"
                ]

                if any(word in text for word in wake_words):

                    print("Jarvis Activated!")
                    return

            except sr.UnknownValueError:
                pass

            except sr.WaitTimeoutError:
                pass

            except Exception as e:
                print("Wake word error:", e)