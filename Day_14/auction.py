print("**********Welcome to Secret Auction *********")

# Step 1 : Ask the user for input
# Step 2 : Save the data into dictionary
# Step 3 : Whether if new bids need to be added 
# Step 4 : Compare bids in dictionary

def find_highest_bidder(bidding):
    winner = ""
    highest_bid = 0

    max(bidding)

    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the highest bid of ₹ {highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? : ")
    price = int(input("What is your bid? :  ₹"))
    bids[name]= price
    to_continue = input("Are there another bidders? Type 'yes' or 'no.: \n").lower()
    if to_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif to_continue == "yes":
        print("\n" *  100)