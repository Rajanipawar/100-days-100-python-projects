from game_data import data
import random

# Format the account data into printable format
def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return (f" {account_name}, a {account_desc}, from {account_country}")

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

  # Make the guess repeatable
score = 0     
should_continue = True
account_b = random.choice(data)
while should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Compare B: {format_data(account_b)}")

    # Ask the user for the guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen 

    print("\n" * 100)
    # Check if user is correct 
    ## Get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## Use if statement to check if user is correct

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # Give user feedback on their guess.
    # Score keeping 
    if is_correct:
        score +=1
        print(f"You're Right. Current Score {score}")
    else:
        print(f"Sorry! That's wrong. Final score is {score}")
        should_continue = False
