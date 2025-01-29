import requests

response = requests.post("http://127.0.0.1:5001/predict",
                         json={"review_text": "This was an absolute disaster of a movie. The plot made no sense, the acting was wooden, and the visuals were dull. I regret wasting two hours of my life on this mess. Definitely a film to skip."})

print(response.json())
# ~/Desktop/RAG-Project/E2E-Setniment on main ?3 > python3 test/api-test.py                                                               py E2E-Setniment at 08: 50: 38 PM
# {'sentiment_prediction': 'positive'}
# ~/Desktop/RAG-Project/E2E-Setniment on main ?3 > python3 test/api-test.py                                                               py E2E-Setniment at 08: 52: 19 PM
# {'sentiment_prediction': 'negative'}
