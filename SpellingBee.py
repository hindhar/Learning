import nltk
nltk.data.path.append('/Users/robhindhaugh/nltk_data')
from nltk.corpus import words

# Get the list of words
english_words = words.words()

# Function to get unique letters from user input
def get_unique_letter(prompt, existing_letters):
    while True:
        letter = input(prompt).strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single alphabetic character.")
        elif letter in existing_letters:
            print("This letter has already been entered. Please try again.")
        else:
            return letter

# Get the central letter
central_letter = get_unique_letter("Enter the central letter: ", [])

# Get the other six letters
other_letters = []
for i in range(6):
    prompt = f"Enter letter {i + 1} of 6: "
    other_letters.append(get_unique_letter(prompt, other_letters + [central_letter]))

# Function to check if a word is a panagram
def is_panagram(word, central, others):
    all_letters = set(others + [central])
    word_set = set(word)
    return word_set.issubset(all_letters) and all(letter in word_set for letter in all_letters)

# Function to check if a word is valid
def is_valid_word(word, central, others):
    if len(word) < 4 or central not in word:
        return False
    all_letters = set(others + [central])
    word_set = set(word)
    return word_set.issubset(all_letters)

# Find and print words
panagrams = []
other_words = []

for word in english_words:
    if is_panagram(word, central_letter, other_letters):
        panagrams.append(word)
    elif is_valid_word(word, central_letter, other_letters):
        other_words.append(word)

print("Panagrams:", panagrams)
print("Other words:", other_words)
