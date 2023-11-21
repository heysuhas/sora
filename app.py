from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = [
    {"user_input": ["hello", "hi", "hey","namaste"], "bot_response": "Hey there!"},
    {"user_input": ["what","your", "name"], "bot_response": "My name is Sora!"},
    {"user_input": ["how", "are", "you"], "bot_response": "I'm great! Thanks for asking."},
    {"user_input": ["bye", "goodbye"], "bot_response": "Goodbye!"},
    {"user_input": ["I", "am", "fine","good"], "bot_response": "Glad to know!"},
    {"user_input": ["who", "developed","you"], "bot_response": "I was developed by Suhas & Varun"},
    {"user_input": ["who", "made","you"], "bot_response": "I was developed by Suhas & Varun"},
]

def get_bot_response(user_input):
    for response in responses:
        if any(word in user_input for word in response["user_input"]):
            return response["bot_response"]
    return "I'm sorry, I didn't understand that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = get_bot_response(user_input.lower())
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
