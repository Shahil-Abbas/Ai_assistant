from speech.wakeword import wait_for_wake_word
import time
from speech.whisper_listen import listen_whisper

from speech.speak import speak

from core.brain import handle_command


while True:

    wait_for_wake_word()

    command = listen_whisper()

    print("You:", command)

    response = handle_command(command)

    if response:

        speak(response)

        time.sleep(1)