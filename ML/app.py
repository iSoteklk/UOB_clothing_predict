from predict import predict_clothing

situation = "party"
color = ""
time = "morning"
gender = "female"
categories = ["t-shirt", "jeans", "shoes", "jacket", "tie"]

predictions = predict_clothing(situation, color, time, gender, categories)

for category, clothing in predictions.items():
    print(f"Predicted clothing for category '{category}': {clothing}")
