# print("********** Welcome to Calculator **********")
# Step 1: Define the basic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("❌ Error! Cannot divide by zero.")
        return None  # Return None to signal an error
    return n1 / n2

# Step 2: Store the operations in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Step 3: Calculator logic
def calculator():
    print("🧮 Welcome to the calculator!")

    num1 = float(input("What's the first number? : "))

    while True:
        # Show available operations
        print("Available operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("❌ Invalid operation. Please choose from +, -, *, /.")
            continue

        num2 = float(input("What's the next number? : "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        # Check if the operation failed (like division by zero)
        if answer is None:
            print("Let's try again.\n")
            continue

        print(f"✅ Result: {num1} {operation_symbol} {num2} = {answer}")

        next_step = input(f"Type 'y' to continue with {answer}, 'n' to start new, or 'exit' to quit: ").lower()

        if next_step == 'y':
            num1 = answer
        elif next_step == 'n':
            print("\n" + "-"*40 + "\n")
            calculator()
            break
        elif next_step == 'exit':
            print("👋 Exiting calculator. Goodbye!")
            break
        else:
            print("❌ Invalid input. Exiting.")
            break

# Start the calculator
calculator()
