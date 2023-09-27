# addition
def add(x, y):
    return x + y

# subtraction
def subtract(x, y):
    return x - y

# multiplication
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    return x / y

while True:
    # Display the menu
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get user's choice
    choice = input("Enter the operation number (1/2/3/4/5): ")

    # Check if the choice is a number
    if choice.isdigit():
        choice = int(choice)
        if choice == 5:
            print("Goodbye!")
            break
        elif choice < 1 or choice > 4:
            print("Invalid choice. Please try again.")
            continue
    else:
        print("Invalid choice. Please try again.")
        continue

    # Get input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation and display the result
    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        result = divide(num1, num2)
        print("Result:", result)