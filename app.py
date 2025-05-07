# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    bot_reply = get_response(user_input)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)

