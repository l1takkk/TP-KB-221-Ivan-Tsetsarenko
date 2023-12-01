from students import Student

class StudentList:
    def __init__(self):
        self.students = []

    def printAllList(self):
        for student in self.students:
            strForPrint = f"Student name is {student.name}, Phone is {student.phone}, Age is {student.age}, Gender is {student.gender}"
            print(strForPrint)
        return

    def addNewElement(self):
        name = input("Pease enter student name: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        gender = input("Please enter student gender: ")
        new_student = Student(name, phone, age, gender)   
        insertPosition = 0
        for student in self.students:
            if name > student.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, new_student)
        print("New element has been added")
        return

    def deleteElement(self):
        name = input("Please enter name to be delated: ")
        deletePosition = -1
        for student in self.students:
            if name == student.name:
                deletePosition = self.students.index(student)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            print("Dele position " + str(deletePosition))
            del self.students[deletePosition]
        return


    def updateElement(self):
        name = input("Please enter name to be updated: ")
        for index, student in enumerate(self.students):
            if name == student.name:
                print("Student found. Please update the information:")
                new_name = input("Please enter new name: ")
                new_phone = input("Please enter new phone number: ")
                new_age = input("Please enter new age: ")
                new_gender = input("Please enter new gender: ")
                new_student = Student(new_name, new_phone, new_age, new_gender)

                del self.students[index]

                insertPosition = 0
                for position, existing_student in enumerate(self.students):
                    if new_name > existing_student.name:
                        insertPosition = position + 1
                    else:
                        break
                self.students.insert(insertPosition,  new_student)
                print("Student information updated.")
                return

        print("Student not found.")
        return