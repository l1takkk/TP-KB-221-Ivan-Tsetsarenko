class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Student name is {self.name}, Phone is {self.phone}"

def printAllList(students):
    for student in students:
        print(student)

def addNewElement(students):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    new_student = Student(name, phone)
    students.append(new_student)
    print("New element has been added")

def deleteElement(students):
    name = input("Please enter name to be deleted: ")
    to_delete = None
    for student in students:
        if name == student.name:
            to_delete = student
            break
    if to_delete:
        students.remove(to_delete)
        print("Element has been deleted")
    else:
        print("Element was not found")

def updateElement(students):
    name = input("Please enter name to be updated: ")
    for student in students:
        if name == student.name:
            print("What do you want to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Both")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                new_name = input("Please enter the new name: ")
                student.name = new_name
            elif choice == 2:
                new_phone = input("Please enter the new phone: ")
                student.phone = new_phone
            elif choice == 3:
                new_name = input("Please enter the new name: ")
                new_phone = input("Please enter the new phone: ")
                student.name = new_name
                student.phone = new_phone
            else:
                print("Invalid choice")
            break
    else:
        print("Element not found")

def main():
    students = [
        Student("Bob", "0631234567"),
        Student("Emma", "0631234567"),
        Student("Jon", "0631234567"),
        Student("Zak", "0631234567")
    ]

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        if choice in ['C', 'c']:
            print("New element will be created:")
            addNewElement(students)
        elif choice in ['U', 'u']:
            print("Existing element will be updated")
            updateElement(students)
        elif choice in ['D', 'd']:
            print("Element will be deleted")
            deleteElement(students)
        elif choice in ['P', 'p']:
            print("List will be printed")
            printAllList(students)
        elif choice in ['X', 'x']:
            print("Exit()")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()