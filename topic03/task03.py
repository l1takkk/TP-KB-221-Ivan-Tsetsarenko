# Функція для додавання пари ключ-значення до словника
def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary

# Функція для видалення ключа та відповідного значення зі словника
def remove_from_dictionary(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

# Функція для пошуку значення за ключем у словнику
def find_by_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return "Ключ не знайдено в словнику"

# Initial dictionary
dictionary = {'один': 1, 'два': 2, 'три': 3}

while True:
    print("Словник:", dictionary)
    print("Оберіть операцію:")
    print("1. Додати ключ та значення до словника")
    print("2. Видалити ключ та відповідне значення зі словника")
    print("3. Знайти значення за ключем у словнику")
    print("4. Вихід")


    operation = input("Введіть номер операції (1/2/3/4): ")

    if operation == '4':
        print("Кінець роботи")
        break

    if operation not in ('1', '2', '3'):
        print("Некоректний вибір операції")
        continue

    if operation == '1':
        key = input("Введіть ключ: ")
        value = input("Введіть значення: ")
        dictionary = add_to_dictionary(dictionary, key, value)
    elif operation == '2':
        key = input("Введіть ключ для видалення: ")
        dictionary = remove_from_dictionary(dictionary, key)
    elif operation == '3':
        key = input("Введіть ключ для пошуку: ")
        result = find_by_key(dictionary, key)
        print("Результат пошуку:", result)