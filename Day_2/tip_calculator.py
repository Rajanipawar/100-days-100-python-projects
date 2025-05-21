print("!!!.....Welcome to Tip Calculator.....!!!")

# Step 1 : Taking inputs
total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 "))
people = int(input("how many people will split the bill? "))

# Step 2 : Calculations (total bill with tip)
bill_with_tip = tip / 100 * total_bill + total_bill
bill_per_person = bill_with_tip / people

# Step 3 : Rounding off to 2 decimals
final_amount = round(bill_per_person , 2)

# Step 4 : Display the results
print(f"Bill with tip is: {bill_with_tip}")
print(f" Each person should pay: {final_amount}")

