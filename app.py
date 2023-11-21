from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = [
    {"user_input": ["hello", "hi", "hey","namaste"], "bot_response": "Hey there! How's it going?😄"},
    {"user_input": ["purpose"], "bot_response": "Hey! I'm here to chat, have fun and help you with anything you need. What's up?"},
    {"user_input": ["color"], "bot_response": "Oh! I love talking about colors! I don't have a specific favourite colors, But I prefer Blue"},
    {"user_input": ["work"], "bot_response": "I analyze your input using natural language processing to generate responses."},
    {"user_input": ["food"], "bot_response": "I don't eat, but I've heard good things about data bytes."},
     {"user_input": ["old", "age"], "bot_response": "I don't have an age in the traditional sense. I'm always up-to-date with the latest information!"},
     {"user_input": ["name", "your"], "bot_response": "My name is Sora!"},
    {"user_input": ["how", "you"], "bot_response": "I'm doing great! Thanks for asking. What about you?"},
    {"user_input": ["bye", "goodbye"], "bot_response": "Aw, already leaving? Well, it was nice chatting with you. Feel free to come back anytime if you want to talk again. Take care and have a great day! 😊👏"},
    {"user_input": ["what", "can", "you", "do"], "bot_response": "I can chat with you, answer questions, tell jokes, and more! Feel free to ask."},
    {"user_input": ["I", "am", "fine","good"], "bot_response": "That's great to hear! You wanna talk about something?😄 "},
    {"user_input": ["thanks", "thank", "you"], "bot_response": "You're welcome! If you have more questions, feel free to ask."},
    {"user_input": ["tell", "me", "a", "joke"], "bot_response": "Sure, here's one: Why did the computer go to therapy? It had too many bytes of emotional danage!"},
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
