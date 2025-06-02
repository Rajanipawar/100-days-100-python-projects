# 🏆 Secret Auction – Day 14 of 100 Days of Python

This project simulates a **Secret Auction** where users can enter their bids without others seeing them.
Once all bids are entered, the program finds and announces the highest bidder.

## 🔧 Concepts Used
- `Dictionaries` for storing bidder names and amounts
- `While loops` to allow multiple users to bid
- `Functions` to find the highest bid
- Conditional logic to determine the winner

## 💻 How it Works

1. The program asks each bidder:
   - Their name
   - Their bid amount
2. Each bid is stored in a dictionary with the name as the key.
3. The screen is cleared after each bid to keep it "secret".
4. Once bidding ends, the program compares all bids and announces the winner.

## 🧪 Sample Output

********** Secret Auction *********
🧑 What is your name? : Raj
💸 What is your bid? ₹2500
🔁 Are there any other bidders? Type 'yes' or 'no': yes

🧑 What is your name? : Meena
💸 What is your bid? ₹3000
🔁 Are there any other bidders? Type 'yes' or 'no': no

🏆 The winner is Meena with the highest bid of ₹3000

## 📁 Project Structure
- `auction.py`: Main Python script

## 📌 Learning Goals
- Understand how to use dictionaries to map user input
- Practice creating functions for data comparison
- Learn how to structure interactive Python CLI programs

## 🚀 Run It Yourself

```bash
python auction.py

