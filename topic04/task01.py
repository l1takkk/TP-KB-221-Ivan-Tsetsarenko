def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Ділення на нуль неможливе")
    return x / y

def GetNumber(prompt):
    while True:
        try:
            x = float(input(prompt))
            return x
        except ValueError:
            print("Некоректне значення, спробуйте ще раз.")

while True:
    print("Choose operation:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")
    
    choice = input("Номер операції (1/2/3/4/5): ")
    
    if choice == "5":
        print("Вихід...")
        break
    
    if choice in ('1', '2', '3', '4'):
        
        FirstNumber = GetNumber("Перше число: ")
        SecondNumber = GetNumber("Друге число: ")

        try:
            if choice == '1':
                result = addition(FirstNumber, SecondNumber)
            elif choice == '2':
                result = subtraction(FirstNumber, SecondNumber)
            elif choice == '3':
                result = multiplication(FirstNumber, SecondNumber)
            elif choice == '4':
                result = division(FirstNumber, SecondNumber)

            print("Результат:", result)
        except ValueError as e:
            print("Помилка:", e)
