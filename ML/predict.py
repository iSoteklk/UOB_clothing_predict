import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import os


def predict_clothing(situation, color, time, gender, categories):
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)
    # Load the trained model
    model_filename = 'clothing_model_1.joblib'
    model = joblib.load(model_filename)

    # Load the vectorizer
    vectorizer_filename = 'count_vectorizer_1.joblib'
    vectorizer = joblib.load(vectorizer_filename)

    predictions = {}

    for category in categories:
        # Vectorize the input
        input_text = ' '.join([situation, color, time, gender, category])
        input_vectorized = vectorizer.transform([input_text])

        # Predict the clothing name
        predicted_clothing = model.predict(input_vectorized)[0]
        predictions[category] = predicted_clothing

    return predictions
