import random

# List of words for the game (you can add more words)
words = ["apple", "banana", "cherry", "dog", "elephant", "flower"]

# Choose a random word from the list
random_word = random.choice(words)

# Initialize variables
guesses = ""
attempts = 6  # You can adjust the number of allowed attempts

# Function to display the current state of the word with underscores for missing letters
def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

# Main game loop
while True:
    # Display the current state of the word
    current_display = display_word(random_word, guesses)
    print("Current word:", current_display)

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the guess has already been made
    if guess in guesses:
        print("You already guessed that letter.")
        continue

    # Add the guess to the list of guesses
    guesses += guess

    # Check if the guess is in the word
    if guess in random_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

    # Check if the player has won or lost
    if display_word(random_word, guesses) == random_word:
        print("Congratulations! You guessed the word:", random_word)
        break
    elif attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", random_word)
        break
