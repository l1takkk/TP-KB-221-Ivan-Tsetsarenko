# Функція для додавання елемента в кінець списку
def add_to_end(lst, element):
    lst.append(element)
    return lst

# Функція для видалення елемента зі списку
def remove(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

# Функція для сортування списку
def sort(lst):
    lst.sort()
    return lst

# Функція для об'єднання двох списків
def concatenate(lst1, lst2):
    result = lst1 + lst2
    return result

# Функція для пошуку елемента у списку
def find(lst, element):
    return element in lst

# Початковий список
my_list = [1, 2, 3, 4, 5]

while True:
    print("Список:", my_list)
    print("Оберіть операцію:")
    print("1. Додати елемент в кінець списку")
    print("2. Видалити елемент зі списку")
    print("3. Відсортувати список")
    print("4. Об'єднати з іншим списком")
    print("5. Пошук елемента в списку")
    print("6. Вихід")

    operation = input("Введіть номер операції (1/2/3/4/5/6): ")

    if operation == '6':
        print("Дякую за використання програми тестування списків!")
        break

    if operation == '1':
        element = int(input("Введіть елемент, який потрібно додати: "))
        my_list = add_to_end(my_list, element)
    elif operation == '2':
        element = int(input("Введіть елемент, який потрібно видалити: "))
        my_list = remove(my_list, element)
    elif operation == '3':
        my_list = sort(my_list)
    elif operation == '4':
        other_list = input("Введіть інший список (розділіть елементи пробілами): ").split()
        my_list = concatenate(my_list, other_list)
    elif operation == '5':
        element = int(input("Введіть елемент, який потрібно знайти: "))
        result = find(my_list, element)
        if result:
            print(f"Елемент {element} знайдено у списку.")
        else:
            print(f"Елемент {element} не знайдено у списку.")