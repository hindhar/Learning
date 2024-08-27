from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return word_list

word_list = load_word_list('../possible_wordle_words.txt')  # Adjusted to reference your existing file
secret_word = random.choice(word_list)

def generate_feedback(secret_word, guess):
    feedback = ['B'] * len(secret_word)
    secret_word_chars = list(secret_word)
    guess_chars = list(guess)

    for i in range(len(secret_word)):
        if guess_chars[i] == secret_word_chars[i]:
            feedback[i] = 'G'
            secret_word_chars[i] = None

    for i in range(len(secret_word)):
        if feedback[i] == 'G':
            continue
        if guess_chars[i] in secret_word_chars:
            feedback[i] = 'Y'
            secret_word_chars[secret_word_chars.index(guess_chars[i])] = None

    return ''.join(feedback)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.json['guess']
    if guess not in word_list:
        return jsonify({'feedback': 'Invalid word!'})
    
    feedback = generate_feedback(secret_word, guess)
    return jsonify({'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True)
