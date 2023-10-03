def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Помилка: ділення на нуль"
    return x / y

while True:
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    operation = input("Введіть номер операції (1/2/3/4/5): ")

    if operation == '5':
        print("Сессія завершена")
        break

    if operation not in ('1', '2', '3', '4'):
        print("Некоректний вибір операції")
        continue

    number1 = float(input("Введіть перше число: "))
    number2 = float(input("Введіть друге число: "))

    if operation == '1':
        print("Результат:", addition(number1, number2))
    elif operation == '2':
        print("Результат:", subtraction(number1, number2))
    elif operation == '3':
        print("Результат:", multiplication(number1, number2))
    elif operation == '4':
        print("Результат:", division(number1, number2))