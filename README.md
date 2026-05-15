# Jarvis AI Assistant

An AI-powered voice assistant built using Python, Ollama, NLP, OpenCV, and CustomTkinter.

## Features

- Wake-word activation using "Jarvis"
- Voice command recognition
- Text-to-speech responses
- AI chatbot using Ollama
- Browser automation
- Camera control with OpenCV
- Weather information
- GUI interface
- Intent detection using NLP

---

# Technologies Used

- Python
- Ollama
- CustomTkinter
- SpeechRecognition
- pyttsx3
- OpenCV
- Scikit-learn
- Requests

---

# Installation

## Create Environment

```bash
conda create -n nlp python=3.10
conda activate nlp
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download from:

https://ollama.com

Pull model:

```bash
ollama pull llama3.2:1b
```

Run model:

```bash
ollama run llama3.2:1b
```

---

# Run Project

```bash
python -m gui.app
```

---

# Voice Commands

## Browser

```text
open chrome and search virat kohli
open edge and search python tutorial
close chrome
close edge
```

## Applications

```text
open notepad
close notepad

open calculator
close calculator
```

## Camera

```text
open camera
close camera
```

## General

```text
what is the time
what is today's date
what is the weather
quit
```

---

# Future Improvements

- Face recognition
- WhatsApp automation
- YouTube automation
- Smart memory system
- Offline speech recognition

---

# Author

Built by Shahil Abbass using Python and Ollama.
