from operations import *

while True:
    print("Виберіть операцію:")
    print("1. Додавання (+)")
    print("2. Віднімання (-)")
    print("3. Множення (*)")
    print("4. Ділення (/)")

    choice = input("Ваш вибір (1/2/3/4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Неправильний вибір операції. Спробуйте ще раз.")
        continue

    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if choice == "1":
        result = perform_addition(num1, num2)
    elif choice == "2":
        result = perform_subtraction(num1, num2)
    elif choice == "3":
        result = perform_multiplication(num1, num2)
    elif choice == "4":
        result = perform_division(num1, num2)

    print(f"Результат: {result}")