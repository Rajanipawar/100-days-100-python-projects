# Step 1 : Import the random module
import random

# Step 2 : Define ASCII art for Rock, Paper, and Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Step 3 : Store the options in a list
game_images = [rock, paper, scissors]

# Step 4 : Get the player's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))

# Step 5 : Display the player’s choice using ASCII
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
else:
    print(f"\nYou chose:\n{game_images[user_choice]}")

# Step 6 : Generate computer’s choice randomly
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computer_choice]}")

# Step 8: Compare choices and decide the winner
    if user_choice == computer_choice:
        print("It's a draw 🤝")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! 🎉 Rock crushes Scissors.")
    elif user_choice == 1 and computer_choice == 0:
        print("You win! 🎉 Paper covers Rock.")
    elif user_choice == 2 and computer_choice == 1:
        print("You win! 🎉 Scissors cut Paper.")
    else:
        print("You lose! 😢")
