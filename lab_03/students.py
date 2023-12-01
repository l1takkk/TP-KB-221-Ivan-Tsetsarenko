class Student:
    def __init__(self, name, phone, age, gender):
        self.name = name
        self.phone = phone
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Student(name='{self.name}', phone='{self.phone}', age={self.age}, gender='{self.gender}')"