import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Read the CSV file into a DataFrame
filename = 'image_data.csv'
df = pd.read_csv(filename)

# Define the input features (X) and target variable (y)
X = df[['situation', 'color', 'type', 'time', 'category', 'gender']].astype(
    str).values.tolist()
y = df['clothing_name']

# Convert text features to numerical representation
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform([' '.join(record) for record in X])

# Train the model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save the trained model
model_filename = 'clothing_model_2.joblib'
joblib.dump(model, model_filename)

# Save the CountVectorizer
vectorizer_filename = 'count_vectorizer_2.joblib'
joblib.dump(vectorizer, vectorizer_filename)

print("Model and CountVectorizer saved successfully.")
