import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    return x / y

while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter the operation number (1/2/3/4/5): ")
    
    match choice:
        case '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", add(num1, num2))
        case '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", subtract(num1, num2))
        case '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Result:", multiply(num1, num2))
        case '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = divide(num1, num2)
            print("Result:", result)
        case '5':
            print("Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")