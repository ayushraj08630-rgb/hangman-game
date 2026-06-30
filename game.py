import random

# List of predefined words
words = ["python", "computer", "program", "intern", "developer"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===================================")
print("      WELCOME TO HANGMAN GAME")
print("===================================")

while wrong_guesses < max_wrong:

    # Display the current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the word is completely guessed
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print(f"Remaining Attempts: {max_wrong - wrong_guesses}")

if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("The correct word was:", word)