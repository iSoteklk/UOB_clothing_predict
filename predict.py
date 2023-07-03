import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model
model_filename = 'clothing_model.joblib'
model = joblib.load(model_filename)

# Load the vectorizer
vectorizer_filename = 'count_vectorizer.joblib'
vectorizer = joblib.load(vectorizer_filename)

# Get user input
situation = input("Enter the situation: ")
color = input("Enter the color: ")

# Vectorize the input
input_text = situation + ' ' + color
input_vectorized = vectorizer.transform([input_text])

# Predict the clothing name
predicted_clothing = model.predict(input_vectorized)[0]
print("Predicted clothing:", predicted_clothing)
