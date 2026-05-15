import whisper
import sounddevice as sd
from scipy.io.wavfile import write

model = whisper.load_model("base")


def listen_whisper():

    fs = 44100

    seconds = 5

    print("Speak now...")

    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1
    )
    sd.wait()

    write("voice.wav", fs, recording)

    result = model.transcribe("voice.wav")

    text = result["text"]

    print("You:", text)

    return text.lower()