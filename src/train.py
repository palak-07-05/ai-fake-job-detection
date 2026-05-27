import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

from src.features import add_features
from src.preprocess import clean_text

# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv("data/fake_job_postings.csv")

print("Dataset Loaded Successfully")
print("Total Rows:", len(df))

# =========================================
# FEATURE ENGINEERING
# =========================================

df = add_features(df)

# =========================================
# CLEAN TEXT
# =========================================

df['text'] = df['text'].apply(clean_text)

# =========================================
# FEATURES & LABELS
# =========================================

X = df['text']
y = df['fraudulent']

# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================================
# TF-IDF VECTORIZER
# =========================================

vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1, 2),
    stop_words='english',
    min_df=2,
    max_df=0.9
)

# Transform text
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# =========================================
# MODEL
# =========================================

model = LogisticRegression(
    max_iter=3000,
    class_weight='balanced'
)

# =========================================
# TRAIN MODEL
# =========================================

print("\nTraining Model...\n")

model.fit(X_train_vec, y_train)

print("Training Completed Successfully")

# =========================================
# PREDICTIONS
# =========================================

preds = model.predict(X_test_vec)

# =========================================
# EVALUATION
# =========================================

accuracy = accuracy_score(y_test, preds)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")

print(classification_report(y_test, preds))

# =========================================
# SAVE MODEL
# =========================================

pickle.dump(model, open("model.pkl", "wb"))

pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nFiles Saved Successfully")
print("model.pkl")
print("vectorizer.pkl")