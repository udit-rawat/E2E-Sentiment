from flask import Flask, request, jsonify, render_template
import joblib
import sqlite3
import logging
import re

# Initialize Flask app
app = Flask(__name__, template_folder="templates")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model and TF-IDF vectorizer
model = joblib.load("research/sentiment_model.pkl")
tfidf = joblib.load("research/tfidf_vectorizer.pkl")

# Database connection
conn = sqlite3.connect("research/imdb_reviews.db", check_same_thread=False)
cursor = conn.cursor()

# Serve the homepage


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Endpoint for sentiment prediction


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data
        data = request.json
        review_text = data.get("review_text", "")

        # Clean and preprocess the text
        cleaned_text = re.sub(r"<.*?>", "", review_text.lower())
        cleaned_text = re.sub(r"[^\w\s]", "", cleaned_text)

        # Transform text using TF-IDF
        text_vector = tfidf.transform([cleaned_text])

        # Predict sentiment
        prediction = model.predict(text_vector)[0]
        logger.info(f"Prediction for review: {review_text} -> {prediction}")

        # Return prediction
        return jsonify({"sentiment_prediction": prediction})

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
