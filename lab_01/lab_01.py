class Student:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Student name is {self.name}, Phone is {self.phone}, Email is {self.email}, Address is {self.address}"

def addNewElement(students):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    new_student = Student(name, phone, email, address)
    students.append(new_student)
    print("New element has been added")

def updateElement(students):
    name = input("Please enter name to be updated: ")
    for student in students:
        if name == student.name:
            print("What do you want to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            print("4. Address")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                new_name = input("Please enter the new name: ")
                student.name = new_name
            elif choice == 2:
                new_phone = input("Please enter the new phone: ")
                student.phone = new_phone
            elif choice == 3:
                new_email = input("Please enter the new email: ")
                student.email = new_email
            elif choice == 4:
                new_address = input("Please enter the new address: ")
                student.address = new_address
            else:
                print("Invalid choice")
            break
    else:
        print("Element not found")

def main():
    students = [
        Student("Bob", "0631234567", "bob@email.com", "123 Main St"),
        Student("Emma", "0631234567", "emma@email.com", "456 Elm St"),
        Student("Jon", "0631234567", "jon@email.com", "789 Oak St"),
        Student("Zak", "0631234567", "zak@email.com", "101 Pine St")
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