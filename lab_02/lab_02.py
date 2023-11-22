import csv
import sys

def load_data(file_name):
    list = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append({"name": row["name"], "phone": row["phone"], "age": row["age"], "gender": row["gender"]})
    return list

def save_data(file_name, list):
    fieldnames = ["name", "phone", "age", "gender"]

    with open(file_name, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)

def printAllList(list):
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Age is " + elem["age"] + ", Gender is " + elem["gender"]
        print(strForPrint)
    return

def addNewElement(list):
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    gender = input("Please enter student gender: ")
    newItem = {"name": name, "phone": phone, "age": age, "gender": gender}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement(list):
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement(list):
    name = input("Please enter name to be updated: ")
    for index, item in enumerate(list):
        if name == item["name"]:
            print("Student found. Please update the information:")
            new_name = input("Please enter new name: ")
            new_phone = input("Please enter new phone number: ")
            new_age = input("Please enter new age: ")
            new_gender = input("Please enter new gender: ")
            new_item = {"name": new_name, "phone": new_phone, "age": new_age, "gender": new_gender}

            del list[index]

            insertPosition = 0
            for position, item in enumerate(list):
                if new_name > item["name"]:
                    insertPosition = position + 1
                else:
                    break
            list.insert(insertPosition, new_item)
            print("Student information updated.")
            return

    print("Student not found.")
    return

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name.csv>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    list = load_data(file_name)

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(list)
                printAllList(list)
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement(list)
                printAllList(list)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(list)
            case "P" | "p":
                print("List will be printed")
                printAllList(list)
            case "X" | "x":
                print("Exit")
                save_data(file_name, list)
                break
            case _:
                print("Wrong choice. Please enter a valid option.")

if __name__ == "__main__":
    main()