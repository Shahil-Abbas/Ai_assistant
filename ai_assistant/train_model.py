import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


with open("data/intents.json") as file:
    data = json.load(file)


texts = []
labels = []

for intent, examples in data.items():

    for example in examples:
        texts.append(example)
        labels.append(intent)


vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

model = LogisticRegression()

model.fit(X, labels)


pickle.dump(model, open("models/intent_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("Model trained successfully")