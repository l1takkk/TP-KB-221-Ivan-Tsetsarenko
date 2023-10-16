import http.client
import json

while True:
    try:
        amount = float(input("Введіть суму в гривнях: "))
        if amount <= 0:
            print("Помилка: Сума повинна бути більше нуля.")
            continue

        currency_code = input("Введіть валюту для конвертації (EUR, USD, AED): ").upper()

        if currency_code not in ["EUR", "USD", "AED"]:
            print("Помилка: Код валюти введений невірно або дана валюта не підтримується. Спробуйте ще раз.")
            continue

        conn = http.client.HTTPSConnection("bank.gov.ua")
        conn.request("GET", f"/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json")
        response = conn.getresponse()
        data = json.loads(response.read().decode("utf-8"))

        if isinstance(data, list) and data:
            rate = data[0]["rate"]
            converted_amount = amount / rate
            print(f"{amount} UAH = {converted_amount:.2f} {currency_code}")
        else:
            print("Помилка при отриманні курсу валюти. Спробуйте ще раз.")
    except ValueError:
        print("Помилка: Введіть коректне число.")