from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of inspirational quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Your limitation—it’s only your imagination.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it."
]

@app.route('/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True)