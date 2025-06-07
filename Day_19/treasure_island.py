print('''
******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to treasure Island!!")
print("Your mission is to find the treasure.")
direction = input("You are at the cross road. Where do you want to go? left or right? ").lower()

if direction == 'left':
    on_lake = input("You have come to lake. There is an island in the middle of the lake. Type 'wait' to see for a boat. Type 'swim' to swim "
                    "across.")
    if on_lake == 'wait':
        door = input("You arrived at the island unharmed. There is a house with three doors. One red, one yellow, one blue. Which colour "
                    "do you chose?  ").lower()
        if door == 'red':
            print("It's a room full of fire. Game over.")
        elif door == 'yellow':
            print("You found the treasure. You win!")
        elif door == 'blue':
            print("You enter the room of beasts. Game over!")
        else:
            print("You chose the door that doesn't exists. Game over.") 
    else:
        print("You got attacked by angry trout. Game over.")
else:
    print("You fell into a hole. Game over!")