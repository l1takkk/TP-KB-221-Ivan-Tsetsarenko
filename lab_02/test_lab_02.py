import unittest
import io
from unittest.mock import patch
from lab_02 import load_data, save_data, addNewElement, deleteElement, updateElement, printAllList

class TestLab2Script(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_lab2.csv"
        self.test_data = [
            {"name": "John", "phone": "9675643454", "age": "21", "gender": "man"},
            {"name": "Alice", "phone": "734586290", "age": "19", "gender": "woman"},
        ]


    def test_load_data(self):
        with open(self.test_file, "w") as file:
            file.write("name,phone,age,gender\nJohn,1234567890,25,male\nAlice,9876543210,22,female")

        data = load_data(self.test_file)
        self.assertEqual(data, [
            {"name": "John", "phone": "1234567890", "age": "25", "gender": "male"},
            {"name": "Alice", "phone": "9876543210", "age": "22", "gender": "female"}
        ])

    def test_save_data(self):
        save_data(self.test_file, self.test_data)
        loaded_data = load_data(self.test_file)
        self.assertEqual(loaded_data, self.test_data)

    def test_addNewElement(self):
        with patch('builtins.input', side_effect=["John", "1234567890", "25", "male"]):
            addNewElement(self.test_data)
            self.assertEqual(len(self.test_data), 3)

    def test_deleteElement(self):
        with patch('builtins.input', return_value="John"):
            deleteElement(self.test_data)
            self.assertEqual(len(self.test_data), 1)

    def test_updateElement(self):
        with patch('builtins.input', side_effect=["John", "Bob", "5555555555", "30", "male"]):
            updateElement(self.test_data)
            self.assertEqual(self.test_data[1]["name"], "Bob")

    def test_printAllList(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(self.test_data)
            output = mock_stdout.getvalue()
            self.assertIn("John", output)
            self.assertIn("Alice", output)

if __name__ == '__main__':
    unittest.main()