import json
import pickle

model = pickle.load(open("models/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

with open("data/intents.json") as file:
    intents = json.load(file)


def predict_intent(text):

    text_vector = vectorizer.transform([text])

    probabilities = model.predict_proba(text_vector)[0]

    max_probability = max(probabilities)

    predicted_index = probabilities.argmax()

    predicted_intent = model.classes_[predicted_index]

    print("Confidence:", max_probability)

    # if confidence low → use Ollama
    if max_probability < 0.60:
        return "unknown"

    return predicted_intent