# E2E-Sentiment: End-to-End Sentiment Analysis Pipeline

**E2E-Sentiment** is an end-to-end sentiment analysis pipeline that processes movie reviews from the IMDb dataset and predicts the sentiment (positive or negative) of a given review. The solution involves data collection, cleaning, exploration, model training, and a Flask API for serving predictions. This project is designed to be easily deployable both on Kaggle and locally.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Folder Structure](#folder-structure)
4. [Setup Instructions](#setup-instructions)
5. [Running the Pipeline](#running-the-pipeline)
6. [Testing the API](#testing-the-api)

---

## Project Overview

This project implements an **End-to-End Sentiment Analysis Pipeline** using the **IMDb** dataset for training a sentiment analysis model. The solution includes:

1. **Data Collection and Preprocessing**: Loading and cleaning data from the IMDb dataset.
2. **Model Training**: Training a sentiment analysis model using **Logistic Regression**.
3. **Flask API**: Creating an API to serve sentiment predictions for new reviews.
4. **Front-end Interface**: A simple web interface built with **Bootstrap 5** to interact with the Flask API.

The pipeline can be tested both on Kaggle and locally.

---

## Technologies Used

- **Python 3.x**
- **Flask**: For creating the REST API.
- **Scikit-learn**: For machine learning models and vectorization.
- **Joblib**: For saving and loading the trained model and vectorizer.
- **SQLite**: For storing and accessing the IMDb reviews dataset.
- **Bootstrap 5**: For building a simple and responsive front-end interface.
- **Requests**: For testing the Flask API.

---

## Setup Instructions

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/udit-rawat/E2E-Sentiment.git
   cd E2E-Sentiment
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure that you have `sentiment_model.pkl` and `tfidf_vectorizer.pkl` files available in your project directory. If not, run the Kaggle notebook `sentiment_analysis_pipeline.ipynb` to train the model and save these files.

---

## Running the Pipeline

1. **Start the Flask API**: Run the following command to start the Flask server:

   ```bash
   python app.py
   ```

   The API will be available at [http://127.0.0.1:5001/](http://127.0.0.1:5001/).

2. **Test the API**: Open `index.html` in a web browser and enter a movie review to see the sentiment prediction.

---

## Testing the API

You can test the Flask API using Python's `requests` library by sending a POST request to the `/predict` endpoint.

Example:

```python
import requests

response = requests.post("http://127.0.0.1:5001/predict", json={"review_text": "This movie was fantastic!"})
print(response.json())
```

Expected Output:

```json
{
  "sentiment_prediction": "positive"
}
```
