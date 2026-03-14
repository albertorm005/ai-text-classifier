import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

datasets = {
    "english": "dataset/english_reviews.csv",
    "spanish": "dataset/spanish_reviews.csv",
    "german": "dataset/german_reviews.csv",
    "french": "dataset/french_reviews.csv"
}

for language, path in datasets.items():

    print(f"Training model for {language}...")

    data = pd.read_csv(path)

    texts = data["text"]
    labels = data["label"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = MultinomialNB()
    model.fit(X, labels)

    joblib.dump((model, vectorizer), f"models/{language}_model.pkl")

print("All models trained and saved!")