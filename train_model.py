import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load dataset
data = pd.read_csv("feedback_data.csv")

X = data["text"]
y = data["label"]

# ML pipeline (STRONGER than Naive Bayes)
model = Pipeline([
    ("vectorizer", TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),   # BIG improvement
        min_df=1
    )),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"  # VERY IMPORTANT
    ))
])

# Train model
model.fit(X, y)

# Save model
with open("feedback_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Logistic Regression model trained and saved")
