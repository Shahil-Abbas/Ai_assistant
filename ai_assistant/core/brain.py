import datetime
import webbrowser
import os
import urllib.parse

from core.intents import predict_intent
from skills.weather import get_weather
from skills.chatbot import ask_ollama
from vision.camera import open_camera, close_camera
import threading

def clean_query(command, remove_words):
    query = command.lower()

    for word in remove_words:
        query = query.replace(word, "")

    return query.strip()


def search_chrome(command):
    query = clean_query(command, [
        "open chrome and search",
        "search chrome for"
    ])

    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    webbrowser.get(chrome_path).open(url)
    return f"Searching Chrome for {query}"


def search_edge(command):
    query = clean_query(command, [
        "open edge and search",
        "search edge for"
    ])

    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"

    webbrowser.get(edge_path).open(url)
    return f"Searching Edge for {query}"


def open_browser_search(command):
    query = clean_query(command, [
        "open browser and search",
        "open google and search",
        "search for",
        "search",
        "and"
    ])

    if query == "":
        return "What should I search?"

    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    webbrowser.open(url)

    return f"Searching Google for {query}"


def close_chrome():
    os.system("taskkill /f /im chrome.exe")
    return "Chrome closed"


def close_edge():
    os.system("taskkill /f /im msedge.exe")
    return "Edge closed"


def handle_command(command):

    command = command.lower()
    print("Received Command:", command)

    # ---------------- SEARCH ----------------

    if "open chrome and search" in command:
        return search_chrome(command)

    elif "open edge and search" in command:
        return search_edge(command)

    elif "open browser and search" in command or "open google and search" in command or "search for" in command:
        return open_browser_search(command)

    # ---------------- BROWSER CONTROL ----------------

    elif "close chrome" in command:
        return close_chrome()

    elif "close edge" in command:
        return close_edge()

    # ---------------- YOUTUBE ----------------

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "close youtube" in command:
        close_chrome()
        return "Closing YouTube"

    # ---------------- GOOGLE ----------------

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "close google" in command:
        close_chrome()
        return "Closing Google"

    # ---------------- NOTEPAD ----------------

    elif "open notepad" in command:
        os.system("start notepad")
        return "Opening Notepad"

    elif "close notepad" in command:
        os.system("taskkill /f /im notepad.exe")
        return "Closing Notepad"

    # ---------------- CALCULATOR ----------------

    elif "open calculator" in command:
        os.system("start calc")
        return "Opening Calculator"

    elif "close calculator" in command:
        os.system("taskkill /f /im CalculatorApp.exe")
        return "Closing Calculator"

    # ---------------- CAMERA ----------------

    elif "open camera" in command:
        threading.Thread(target=open_camera).start()
        return "Opening camera"

    elif "close camera" in command:
        close_camera()
        return "Closing camera"

    # ---------------- EXIT ----------------

    elif "exit" in command or "quit" in command:
        return "EXIT"

    # ---------------- INTENT PREDICTION ----------------

    intent = predict_intent(command)
    print("Detected Intent:", intent)

    if intent == "time":
        return datetime.datetime.now().strftime("%I:%M %p")

    elif intent == "date":
        return datetime.datetime.now().strftime("%d %B %Y")

    elif intent == "identity":
        return "I am Jarvis, your AI assistant."

    elif intent == "weather":
        return get_weather("Kochi")

    elif intent == "unknown":
        return ask_ollama(command)

    # ---------------- OLLAMA FALLBACK ----------------

    return ask_ollama(command)