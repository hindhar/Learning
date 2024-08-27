import random

def load_word_list(file_path):
    """Load the list of possible words from a file."""
    with open(file_path, 'r') as file:
        word_list = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return word_list

def generate_feedback(secret_word, guess):
    """Generate feedback for a guess based on the secret word."""
    feedback = ['B'] * len(secret_word)
    secret_word_chars = list(secret_word)
    guess_chars = list(guess)

    # First pass: Check for correct letters in the correct positions (Green)
    for i in range(len(secret_word)):
        if guess_chars[i] == secret_word_chars[i]:
            feedback[i] = 'G'
            secret_word_chars[i] = None  # Mark this as used

    # Second pass: Check for correct letters in the wrong positions (Yellow)
    for i in range(len(secret_word)):
        if feedback[i] == 'G':
            continue
        if guess_chars[i] in secret_word_chars:
            feedback[i] = 'Y'
            secret_word_chars[secret_word_chars.index(guess_chars[i])] = None

    return ''.join(feedback)

def play_wordle(secret_word, word_list, max_attempts=6):
    """Simulate a game of Wordle."""
    attempts = 0
    print("Welcome to Wordle!")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: ").lower()

        if len(guess) != len(secret_word):
            print(f"Your guess must be {len(secret_word)} letters long.")
            continue

        if guess not in word_list:
            print("Invalid word! Please enter a valid 5-letter word.")
            continue

        feedback = generate_feedback(secret_word, guess)
        print("Feedback:", feedback)

        if feedback == 'G' * len(secret_word):
            print(f"Congratulations! You've guessed the word {secret_word} correctly!")
            return True

        attempts += 1

    print(f"Sorry, you've used all your attempts. The word was {secret_word}.")
    return False

def main():
    # File path to the list of possible Wordle words
    file_path = '/Users/robhindhaugh/Documents/GitHub/Learning/games/Wordle Solver/possible_wordle_words.txt'

    # Load the list of possible words from the file
    word_list = load_word_list(file_path)

    # Randomly select a 5-letter secret word from the list
    secret_word = random.choice(word_list)

    # Start the game
    play_wordle(secret_word, word_list)

if __name__ == "__main__":
    main()