import random

def hangman():
    words = ["python", "apple", "school", "program", "india"]  # 5 predefined words
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word letter by letter.")
    print("You have 6 incorrect attempts.\n")

    while attempts > 0:
        print("Word:", " ".join(guessed))
        print("Wrong attempts left:", attempts)
        print("Guessed letters:", guessed_letters)

        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("Wrong guess!\n")
            attempts -= 1

        if "_" not in guessed:
            print("You won! The word was:", word)
            return

    print("Game Over! The word was:", word)

# Run the game
hangman()
