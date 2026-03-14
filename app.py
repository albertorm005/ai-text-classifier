from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

languages = {
    "english": "models/english_model.pkl",
    "spanish": "models/spanish_model.pkl",
    "german": "models/german_model.pkl",
    "french": "models/french_model.pkl"
}

@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None

    if request.method == "POST":

        text = request.form["text"].lower().strip()
        language = request.form["language"]

        model, vectorizer = joblib.load(languages[language])

        vector = vectorizer.transform([text])

        prediction = model.predict(vector)[0]

        probabilities = model.predict_proba(vector)

        confidence = round(max(probabilities[0]) * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)