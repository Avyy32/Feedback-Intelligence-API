from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Feedback Intelligence API")
@app.get("/health")
def health():
    return {"status": "ok"}

# Load trained model
with open("feedback_model.pkl", "rb") as f:
    model = pickle.load(f)

class FeedbackInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "Feedback Intelligence API is running"}

@app.post("/analyze")
def analyze_feedback(input: FeedbackInput):

    probs = model.predict_proba([input.text])[0]
    max_confidence = float(np.max(probs))
    model_prediction = model.classes_[np.argmax(probs)]

    # Confidence threshold
    THRESHOLD = 0.4  # tuned for small datasets

    if max_confidence < THRESHOLD:
        final_category = "uncertain"
    else:
        final_category = model_prediction

    return {
        "category": final_category,
        "model_prediction": model_prediction,
        "confidence_score": round(max_confidence, 2)
    }
