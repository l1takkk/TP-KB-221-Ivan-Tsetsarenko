import sys
from fileManager import FileManager

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name.csv>")
        sys.exit(1)
        
    file_name = sys.argv[1]
    list = FileManager.load_data(file_name)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                list.addNewElement()
                list.printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                list.updateElement()
                list.printAllList()
            case "D" | "d":
                print("Element will be deleted")
                list.deleteElement()
            case "P" | "p":
                print("List will be printed")
                list.printAllList()
            case "X" | "x":
                print("Exit")
                FileManager.save_data(file_name, list)
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()
