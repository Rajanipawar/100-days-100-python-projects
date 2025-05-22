print("!!!.....Welcome to Coco Pizza Diliveries.....!!!")

# Step 1 : Take user inputs 
size = input("What size of pizza do you want? S, M, or L : ").upper()
pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N : ").upper()

#Step 2 :  Base calculation

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid pizza size selected!!")

# Step 3 : Add-ons

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

# Step 4 : Final Output

print(f"\nYour total bill is : {bill}")