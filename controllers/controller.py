# controllers/controller.py
import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import copy
import numpy as np


def load_model_and_vectorizer():
    # Get the absolute path of the current module (controller.py)
    module_path = os.path.dirname(os.path.abspath(__file__))

    # Construct absolute file paths for the model and vectorizer
    model_filename = os.path.join(
        module_path, '..', 'ML', 'clothing_model_2.joblib')
    vectorizer_filename = os.path.join(
        module_path, '..', 'ML', 'count_vectorizer_2.joblib')

    # Load the trained model and vectorizer
    model = joblib.load(model_filename)
    vectorizer = joblib.load(vectorizer_filename)
    return model, vectorizer


async def predict_clothing(situation, color, time, gender, type, categories):
    data = []

    i = 0

    while i < 5:
        # Load the model and vectorizer at each iteration
        model, vectorizer = load_model_and_vectorizer()

        predictions = {}
        for category in categories:
            # Vectorize the input
            input_text = ' '.join(
                [situation, color, time, gender, type, category])
            input_vectorized = vectorizer.transform([input_text])

            # Predict the clothing name probabilities
            prediction_probs = model.predict_proba(input_vectorized)[0]

            # Get the index of the next-best prediction
            best_idx = np.argsort(-prediction_probs)[i]

            # Get the name of the next-best predicted clothing
            next_best_prediction = model.classes_[best_idx]
            predictions[category] = next_best_prediction

        data.append(predictions)
        i = i + 1

    return data
