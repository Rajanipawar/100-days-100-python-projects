import time

# Step 1: Get user input for countdown start
start = int(input("Enter the number to start the countdown from: "))

# Step 2: Validate input
if start <= 0:
    print("Please enter a number greater than 0 to start the countdown.")
else:
    print("\n--- Countdown Begins ---")
    # Step 3: Countdown using a while loop
    while start > 0:
        print(start)
        time.sleep(1)
        start -= 1

    # Step 4: Print final message
    print("🎉 Countdown Complete! 🎉")
