from predict import predict_clothing

situation = "party"
color = "Red"
time = "morning"
gender = "female"
type = "formal"
categories = ["t-shirt", "jeans", "shoes", "jacket", "tie"]

predictions = predict_clothing(
    situation, color, time, gender, type, categories)

for category, clothing in predictions.items():
    print(f"Predicted clothing for category '{category}': {clothing}")
