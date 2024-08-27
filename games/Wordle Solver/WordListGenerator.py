import nltk
import os

# Ensure you have downloaded the word list from nltk
nltk.download('words')

# Get the list of words from the nltk corpus
from nltk.corpus import words
word_list = words.words()

# Filter the list to only include 5-letter words
possible_wordle_words = [word.lower() for word in word_list if len(word) == 5 and word.isalpha()]

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the output file path
output_file_path = os.path.join(script_dir, 'possible_wordle_words.txt')

# Save the list to the specified file
with open(output_file_path, 'w') as file:
    for word in possible_wordle_words:
        file.write(word + '\n')

print(f"Number of possible Wordle answers: {len(possible_wordle_words)}")
print(f"List of possible Wordle words saved to '{output_file_path}'")
