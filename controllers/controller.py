# controllers/controller.py
import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer


def load_model_and_vectorizer():
    # Get the absolute path of the current module (controller.py)
    module_path = os.path.dirname(os.path.abspath(__file__))

    # Construct absolute file paths for the model and vectorizer
    model_filename = os.path.join(
        module_path, '..', 'ML', 'clothing_model_1.joblib')
    vectorizer_filename = os.path.join(
        module_path, '..', 'ML', 'count_vectorizer_1.joblib')

    # Load the trained model and vectorizer
    model = joblib.load(model_filename)
    vectorizer = joblib.load(vectorizer_filename)
    return model, vectorizer


async def predict_clothing(situation, color, time, gender, categories):
    model, vectorizer = load_model_and_vectorizer()

    predictions = {}

    for category in categories:
        # Vectorize the input
        input_text = ' '.join([situation, color, time, gender, category])
        input_vectorized = vectorizer.transform([input_text])

        # Predict the clothing name
        predicted_clothing = model.predict(input_vectorized)[0]
        predictions[category] = predicted_clothing

    return predictions
