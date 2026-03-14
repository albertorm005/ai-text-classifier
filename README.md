# 🌍 AI Multilingual Sentiment Classifier

This project is a **Machine Learning application for sentiment analysis** that can classify text as **positive or negative** in multiple languages.

The classifier supports:

- English 🇬🇧
- Spanish 🇪🇸
- German 🇩🇪
- French 🇫🇷

The system trains a separate model for each language and loads the appropriate model depending on the user's selection.

---

# 🚀 Features

- Multilingual sentiment analysis
- Separate datasets for each language
- Machine learning model training
- Saved trained models using `joblib`
- Interactive CLI interface
- Real-time text prediction

---

# 🧠 Machine Learning Model

The project uses:

- **TF-IDF Vectorization** for text feature extraction
- **Multinomial Naive Bayes** for classification

Each language has its own trained model.

---

# 📂 Project Structure


ai-text-classifier
│
├── dataset
│ ├── english_reviews.csv
│ ├── spanish_reviews.csv
│ ├── german_reviews.csv
│ └── french_reviews.csv
│
├── model
│ └── train_model.py
│
├── models
│ ├── english_model.pkl
│ ├── spanish_model.pkl
│ ├── german_model.pkl
│ └── french_model.pkl
│
├── predict.py
├── requirements.txt
└── README.md


---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-text-classifier.git
cd ai-text-classifier

Install dependencies:

pip install -r requirements.txt
🏋️ Training the Models

To train the machine learning models:

python model/train_model.py

This will generate the trained models inside the models folder.

💻 Running the Classifier

Run the prediction script:

python predict.py

Example:

AI Sentiment Classifier

Choose language:
1 English
2 Spanish
3 German
4 French

Enter number: 2
Enter a sentence: me encanta este juego

Predicted sentiment: positive
📊 Dataset

Each language dataset contains 50 labeled sentences:

25 positive

25 negative

This allows the model to learn basic sentiment patterns for each language.

⚠️ Limitations

The dataset used for training is relatively small. Because of this, predictions may not always be perfectly accurate for unseen vocabulary.

Increasing the dataset size would significantly improve model performance.

🛠 Technologies Used

Python

Pandas

Scikit-learn

Joblib

TF-IDF

Naive Bayes

📌 Future Improvements

Possible improvements for this project:

Add more training data

Support more languages

Build a web interface with Flask

Use more advanced NLP models (BERT, transformers)

👨‍💻 Author

Developed as a Machine Learning portfolio project.