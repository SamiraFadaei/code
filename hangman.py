import random

words = ["PYTHON", "APPLE", "HOUSE", "MOUSE", "TRAIN", "PHONE"]
word = random.choice(words)

guessed = []
lives = 3

hangman = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
"""
]

print("===== HANGMAN =====")

while lives > 0:

    print(hangman[3 - lives])

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if "_" not in display:
        print("\n🎉 YOU WIN!")
        break

    guess = input("Guess a letter: ").upper()

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")
    else:
        lives -= 1
        print("Wrong!")
        print("Lives left:", lives)

if lives == 0:
    print(hangman[3])
    print("\n💀 GAME OVER!")
    print("The word was:", word)