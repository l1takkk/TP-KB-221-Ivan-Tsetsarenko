import unittest
from students import Student
from students2 import StudentList
from fmanager import FileManager
from unittest import TestCase, mock

class TestFileManagerMethods(unittest.TestCase):

    def test_load_data(self):
        test_file = "test_file.csv"
        with open(test_file, "w") as file:
            file.write("name,phone,age,gender\nVanya,1234567890,19,man")
        student_list = FileManager.load_data(test_file)
        self.assertEqual(len(student_list.students), 1)

    @mock.patch("builtins.input", side_effect=["Vanya", "1234567890", "19", "man"])
    def test_save_data(self, mock_input):
        test_file = "test_file.csv"
        student_list = StudentList()
        student_list.addNewElement()
        FileManager.save_data(test_file, student_list)
        with open(test_file, "r") as file:
            content = file.read()
            self.assertIn("Anna", content)

class TestStudentListMethods(unittest.TestCase):

    @mock.patch("builtins.input", side_effect=["Vanya", "1234567890", "19", "man"])
    def test_addNewElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        self.assertEqual(len(student_list.students), 1)
        self.assertEqual(student_list.students[0].name, "Vanya")

    @mock.patch("builtins.input", return_value="Vanya")
    def test_deleteElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        student_list.deleteElement()
        self.assertEqual(len(student_list.students), 0)

    @mock.patch("builtins.input", side_effect=["Vanya", "Denchik", "0664328866", "20", "man"])
    def test_updateElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        student_list.updateElement()
        self.assertEqual(student_list.students[0].name, "Denchik")
if __name__ == '__main__':
    unittest.main()