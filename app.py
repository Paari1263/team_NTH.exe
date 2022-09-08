from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
from googletrans import Translator
import cgi

translator = Translator()
app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    print(request.get_json())
    lan = translator.detect(text).lang
    translation1 = translator.translate(text, dest='en')
    response = get_response(translation1.text)
    translation2 = translator.translate(response, dest=lan)
    message = {"answer": translation2.text}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)