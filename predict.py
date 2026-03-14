import joblib

languages = {
    "1": "english",
    "2": "spanish",
    "3": "german",
    "4": "french"
}

print("AI Sentiment Classifier")
print("----------------------")
print("Choose language:")
print("1 English")
print("2 Spanish")
print("3 German")
print("4 French")

choice = input("Enter number: ")

language = languages.get(choice)

if language is None:
    print("Invalid option")
    exit()

model, vectorizer = joblib.load(f"models/{language}_model.pkl")

text = input("Enter a sentence: ").lower().strip()

vector = vectorizer.transform([text])

prediction = model.predict(vector)

print("Predicted sentiment:", prediction[0])