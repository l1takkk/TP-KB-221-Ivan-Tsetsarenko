data = [{'name': 'Toyota', 'model': 'Chaser'},
        {'name': 'Honda', 'model': 'Civic'},
        {'name': 'Chevrolet', 'model': 'Corvette'},
        {'name': 'VAZ', 'model': '21099'},
        {'name': 'Nissan', 'model': 'Skyline'},
        {'name': 'Lexus', 'model': 'IS300'},
        {'name': 'Mazda', 'model': 'RX-7'},
        {'name': 'Subaru', 'model': 'Impreza'}]

reverse_sort = input("Сортувати в алфавітному порядку (yes/no)? ").lower()
reverse = reverse_sort != 'yes'

sort_by = input("Сортувати за назвами марок (name) чи назвами моделей (model)? ").lower()
if sort_by not in ['name', 'model']:
    print("Неправильний ключ сортування.")
else:
    def alphabetically_reverse(word):
        if reverse:
            return word[::-1]
        else:
            return word

    sorted_data = sorted(data, key=lambda x: alphabetically_reverse(x[sort_by]))

    for item in sorted_data:
        print(f"Name: {item['name']}, Model: {item['model']}")