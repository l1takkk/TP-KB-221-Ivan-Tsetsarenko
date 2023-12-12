import csv
from students import Student
from students2 import StudentList

class FileManager:
    def load_data(file_name):
            list = StudentList()
            with open(file_name) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row["name"], row["phone"], row["age"], row["gender"])
                    list.students.append(student)
            return list

    def save_data(file_name, list):
        fieldnames = ["name", "phone", "age", "gender"]
        with open(file_name, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in list.students:
                writer.writerow({"name": student.name, "phone": student.phone, "age": student.age, "gender": student.gender})