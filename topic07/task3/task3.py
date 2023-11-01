import os

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def save_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"name: {item.name}, age: {item.age}\n")

def main():
    students = [
        Student("Vanya", 20),
        Student("Dima", 22),
        Student("Artem", 19),
        Student("Denis", 21)
    ]

    print("Список студентів:")
    for student in students:
        print(f"name: {student.name}, age: {student.age}")

    sort_choice = input("Бажаєте сортувати за 'ім'ям' чи 'віком'? ")

    if sort_choice == 'ім\'ям':
        students = sorted(students, key=lambda x: x.name)
    elif sort_choice == 'віком':
        students = sorted(students, key=lambda x: x.age)
    else:
        print("Неправильний вибір сортування.")

    if students:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = input(f"Введіть назву файлу для збереження у теку {current_directory}: ") + ".txt"
        file_path = os.path.join(current_directory, file_name)

        if os.path.exists(file_path):
            print(f"Файл з іменем {file_name} вже існує. Будь ласка, виберіть інше ім'я файлу.")
        else:
            save_to_file(file_path, students)
            print(f"Файл {file_name} успішно збережено.")

if __name__ == "__main__":
    main()
