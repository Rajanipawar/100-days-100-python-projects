#  Choosing the random number between 1 and 100
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users guess against actual number

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns

#  Function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': " )
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
#  Let the user to guess the number
def game():
    print("********** Welcome to the Guessing Game! **********")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    # print(f"Psssst, the correct answer is {answer}")

    turns = set_difficulty()

# Repeat the guessing functionality if they get it wrong

    guess = None
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if guess == answer:
            break
        if turns == 0:
            print(f"You're out of guesses! The answer was {answer}.")
            break
        else:
            print("Guess again.")
game()