# Step 1 : import modules 

import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
lives = 6

# Step 2 : To store correctly guessed letters
display = ["_" for _ in chosen_word]
guessed_letters = []

print("********** Welcome to Hangman! **********")

# Step 3 : Main Game Loop
while lives > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Good guess! ")
    else:
        lives -= 1
        print(f"Wrong guess! You lose a life. Lives left: {lives}")

    print("Current word: ", " ".join(display))
    print(stages[6 - lives])  # To show correct stage

# Step 4 : Final Result
if "_" not in display:
    print("********** You Win! **********")
else:
    print(f"********** You Lose. The word was: {chosen_word} **********")
