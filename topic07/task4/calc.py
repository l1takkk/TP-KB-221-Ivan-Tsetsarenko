import logging
from operations import perform_addition, perform_subtraction, perform_multiplication, perform_division

# Клас для додавання
class Addition:
    @staticmethod
    def operate(a, b):
        return a + b

# Клас для віднімання
class Subtraction:
    @staticmethod
    def operate(a, b):
        return a - b

# Клас для множення
class Multiplication:
    @staticmethod
    def operate(a, b):
        return a * b

# Клас для ділення
class Division:
    @staticmethod
    def operate(a, b):
        if b == 0:
            raise ValueError("Ділення на нуль недопустиме")
        return a / b

# Основний клас калькулятору
class Calculator:
    def __init__(self):
        self.operations = {
            "1": Addition(),
            "2": Subtraction(),
            "3": Multiplication(),
            "4": Division()
        }
        logging.basicConfig(filename='calculator.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def calculate(self):
        while True:
            print("Виберіть операцію:")
            print("1. Додавання (+)")
            print("2. Віднімання (-)")
            print("3. Множення (*)")
            print("4. Ділення (/)")

            choice = input("Ваш вибір (1/2/3/4): ")

            if choice not in self.operations:
                print("Неправильний вибір операції. Спробуйте ще раз.")
                continue

            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))

            operation = self.operations[choice]
            try:
                result = operation.operate(num1, num2)
                logging.info(f'{operation.__class__.__name__}: {num1} {choice} {num2} = {result}')
            except ValueError as e:
                print(f"Помилка: {e}")
                logging.error(f'Помилка: {e}')
                continue

            print(f"Результат: {result}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculate()
