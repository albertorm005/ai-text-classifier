import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer()

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    predictions = model.predict(X_test_vec)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{language} model accuracy: {accuracy:.2f}")

    joblib.dump((model, vectorizer), f"models/{language}_model.pkl")

print("All models trained and saved!")