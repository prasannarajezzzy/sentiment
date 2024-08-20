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
    
@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
