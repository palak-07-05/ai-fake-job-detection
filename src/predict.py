import pickle
import os

from src.preprocess import clean_text
import config

# =========================================
# LOAD MODEL & VECTORIZER
# =========================================

if not os.path.exists(config.MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {config.MODEL_PATH}")

if not os.path.exists(config.VECTORIZER_PATH):
    raise FileNotFoundError(f"Vectorizer file not found: {config.VECTORIZER_PATH}")

model = pickle.load(open(config.MODEL_PATH, "rb"))
vectorizer = pickle.load(open(config.VECTORIZER_PATH, "rb"))

# =========================================
# PREDICTION FUNCTION
# =========================================

def predict_job(text):

    # Empty input handling
    if not text or len(text.strip()) == 0:
        return {
            "prediction": -1,
            "fake_score": 0,
            "real_score": 0,
            "message": "Empty job description"
        }

    # Clean text
    cleaned = clean_text(text)

    # Vectorize
    vector = vectorizer.transform([cleaned])

    # Prediction
    pred = model.predict(vector)[0]

    # Probability scores
    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(vector)[0]

        real_score = round(probabilities[0] * 100, 2)
        fake_score = round(probabilities[1] * 100, 2)

    else:
        real_score = 0
        fake_score = 0

    # Final result
    return {
        "prediction": int(pred),
        "fake_score": fake_score,
        "real_score": real_score
    }