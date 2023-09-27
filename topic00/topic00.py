# task n1
input_str = "abcdefg123"
reversed_str = input_str[::-1]
print("Зворотній рядок:", reversed_str)

# task n2
test_str = "Текст для тестування рядків"
print("Довжина:", len(test_str))
print("Перший символ:", test_str[0])
print("Останній символ:", test_str[-1])
print("Індекс рядків:", test_str.find("тексту"))
print("Заміна тексту на рядки':", test_str.replace("тексту", "рядки"))

# task n3
def обчислити_дискримінант(a, b, c):
    дискримінант = b**2 - 4*a*c
    return дискримінант

a = 2
b = 5
c = 1

дискримінант = обчислити_дискримінант(a, b, c)
print("Дискримінант:", дискримінант)