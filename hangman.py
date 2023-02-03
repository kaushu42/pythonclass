# Hangman:
# Author: Kaushal
import random


def get_all_indices(string, char):
    """Searches a string for a character and returns the corresponding indices"""
    return [index for index, value in enumerate(string) if value == char]


def print_game_prompt(display_string, n_guesses):
    """Display the main game screen"""
    print("="*20)
    print("".join(display_string))
    print(f"{n_guesses} lives left.")
    print("="*20)


def get_and_validate_input():
    """Gets input from the user. If the user enters an invalid guess, the 
    function returns None. Else, it returns the character typed by the user."""
    char = input("Guess a Letter: ").lower()
    if len(char) != 1:
        print("!!!!Invalid input, enter a single character!!!!")
        return None
    return char


# The list of words to choose randomly from
words = ["Apple", "Ball", "Mississippi", "Kaushal", "Python"]
word = random.choice(words)

# Converting to lowercase for easy match checking later on
lower_word = word.lower()

# This set holds all the user's guessed characters.
# If they guess the same character again, we don't want to reduce their lives
guessed = set()

# The list that is displayed on the screen
# It will be updated as the user guesses the letters correctly
display_string = ["-"] * len(word)

# The number of guesses allowed to the user
n_guesses = 3

# Loop until the user runs out of lives
while n_guesses > 0:
    # Display the message
    print_game_prompt(display_string, n_guesses)

    # Get the user input and get input again if the input is invalid
    char = get_and_validate_input()
    if char is None:
        continue

    # If the character has already been guessed, continue
    if char in guessed:
        print(f"You already guessed '{char}'. Enter another guess.")
        continue

    # If the character hasn't been guessed, add it to the guessed set
    guessed.add(char)

    # Check if character exists in the word
    if char in lower_word:
        # If it exists, get all the possible indices.
        # This is done to also allow words having duplicate letters
        indices = get_all_indices(lower_word, char)

        # Update the display string if the guess is correct
        for i in indices:
            display_string[i] = char

        # If there are no empty spaces in the display string, we can just exit
        if "-" not in display_string:
            break
    else:
        # If the user guessed incorrectly, decrease the number of lives
        n_guesses -= 1
        print("Wrong guess!")

# Check n_guesses and display a "WON" or "LOST" message
print("="*20)
if n_guesses == 0:
    print(f"You lost! The word was '{word}'.")
else:
    print(f"You won! The word was '{word}'.")
print("="*20)



#Test
