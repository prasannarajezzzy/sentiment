import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Set up your API URL and headers
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json(),"ssssssssssssss")
    return response.json()[0]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    response = query({"inputs": user_message})
    response_text = response[0]['label']
    response_text = "The given response is :" + response_text
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)




# from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
# import torch
# # Load the pre-trained model and tokenizer
# model_name = "distilbert-base-uncased-finetuned-sst-2-english"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

# # Create a sentiment-analysis pipeline
# sentiment_analyzer = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


# from flask import Flask, render_template, request, jsonify
# from transformers import pipeline

# app = Flask(__name__)

# # Load the pre-trained model for conversational AI
# chatbot = sentiment_analyzer

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get_response", methods=["POST"])
# def get_response():
#     user_message = request.json.get("message")
#     response = chatbot(user_message)
#     print(response)
#     response_text = response[0]['label']
#     response_text= "The given response is :"+response_text
#     return jsonify({"response": response_text})

# if __name__ == "__main__":
#     app.run(debug=True)

