# 🧠 Feedback Intelligence API (AI/ML Backend)

A **Machine Learning–powered backend API** that analyzes customer feedback text and classifies it into meaningful business categories, along with a confidence score.

This project demonstrates how **AI models can be safely integrated into real-world backend systems** using confidence-aware predictions.

---

## 🚀 What This Project Does

- Accepts raw customer feedback as text  
- Uses a trained ML model to classify feedback intent  
- Returns:
  - Predicted category
  - Model confidence score
  - Safe fallback for low-confidence cases  
- Exposes functionality via a REST API using **FastAPI**

---

## 🧠 Feedback Categories

The API classifies feedback into the following categories:

- **praise** – positive feedback or appreciation  
- **complaint** – negative experiences or issues  
- **suggestion** – feature requests or improvements  
- **neutral** – informational or non-opinionated feedback  
- **uncertain** – returned when model confidence is low  

> Low-confidence predictions are intentionally marked as **uncertain** to avoid incorrect automated decisions.

---

## 📌 Example API Responses

### ✅ Confident Prediction

```json
{
  "category": "complaint",
  "model_prediction": "complaint",
  "confidence_score": 0.62
}



## 📌 Example API Responses

### ✅ Confident Prediction

```json
{
  "category": "complaint",
  "model_prediction": "complaint",
  "confidence_score": 0.62
}

⚠️ Ambiguous Input
{
  "category": "uncertain",
  "model_prediction": "praise",
  "confidence_score": 0.28
}
⚙️ Tech Stack

Python

FastAPI

scikit-learn

TF-IDF Vectorizer

Logistic Regression

REST API

Swagger UI

📁 Project Structure
feedback-intelligence-api/
├── main.py                 # FastAPI backend
├── train_model.py          # ML training script
├── feedback_data.csv       # Training dataset
├── feedback_model.pkl      # Trained model
├── requirements.txt
└── README.md

🔍 API Endpoints
🔹 Analyze Feedback

POST /analyze

Request

{
  "text": "The app crashes frequently and support never responds"
}


Response

{
  "category": "complaint",
  "model_prediction": "complaint",
  "confidence_score": 0.61
}

🔹 Health Check

GET /health

Response

{
  "status": "ok"
}


Used by deployment platforms and monitoring systems to verify service availability.

🌍 Real-World Use Cases

Customer feedback analysis dashboards

Support ticket prioritization

Product review monitoring

SaaS user feedback intelligence

Survey and form response analysis

⚠️ Design Philosophy (Important)

This project prioritizes safety and transparency over forced accuracy.

Predictions with low confidence are flagged as uncertain

Confidence scores are exposed to support human decision-making

Mirrors how ML systems are used in production environments

▶️ Running Locally
pip install -r requirements.txt
uvicorn main:app --reload


Open Swagger UI:

https://feedback-intelligence-api.onrender.com/docs


📌 Project Status

Version: v2

Status: Complete

Next Planned Improvement:

Larger dataset

Multi-stage classification
