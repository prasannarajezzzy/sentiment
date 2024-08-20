from flask import Flask
import requests
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


# Set up your API URL and headers
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json(),"ssssssssssssss")
    return response.json()[0]

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    response = query({"inputs": user_message})
    response_text = response[0]['label']
    response_text = "The given response is :" + response_text
    return jsonify({"response": response_text})

    
@app.route('/')
def homepage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
