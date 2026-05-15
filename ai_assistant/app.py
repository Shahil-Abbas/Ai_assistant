import customtkinter as ctk
import threading

from speech.listen import listen
from speech.speak import speak
from core.brain import handle_command
from speech.wakeword import wait_for_wake_word


app = ctk.CTk()
app.geometry("500x400")
app.title("Jarvis AI")

label = ctk.CTkLabel(app, text="Jarvis AI Assistant", font=("Arial", 24))
label.pack(pady=20)

status_label = ctk.CTkLabel(app, text="Say 'Jarvis' to activate")
status_label.pack(pady=5)

textbox = ctk.CTkTextbox(app, width=400, height=220)
textbox.pack(pady=20)


def add_text(text):
    textbox.insert("end", text)
    textbox.see("end")


def process_command():
    status_label.configure(text="Listening for command...")

    command = listen()

    if command == "":
        add_text("Jarvis: Sorry, I did not hear anything.\n\n")
        speak("Sorry, I did not hear anything")
        status_label.configure(text="Say 'Jarvis' to activate")
        return

    response = handle_command(command)

    add_text(f"You: {command}\n")

    if response == "EXIT":
        add_text("Jarvis: Shutting down...\n\n")
        speak("Shutting down")
        app.after(1000, app.destroy)
        return

    add_text(f"Jarvis: {response}\n\n")
    speak(response)

    status_label.configure(text="Say 'Jarvis' to activate")


def wakeup_loop():
    while True:
        status_label.configure(text="Waiting for wake word: Jarvis")
        wait_for_wake_word()

        status_label.configure(text="Jarvis activated!")
        speak("Yes, I am listening")

        process_command()


def start_wakeup():
    thread = threading.Thread(target=wakeup_loop, daemon=True)
    thread.start()


start_wakeup()

app.mainloop()