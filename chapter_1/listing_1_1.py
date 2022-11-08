import requests

# веб запрос ограничен производительностью ввода-вывода
response = requests.get(url="https://ya.ru/")

items = response.headers.items()

# обработка ответа ограничена быстродействием процессора
headers = [f"{key}: {header}" for key, header in items]

# конкатенация строк ограничена быстродействием процессора
formatted_headers = "\n".join(headers)

# запись на диск ограничена производительностью ввода-вывода
with open(file="headers.txt", mode="w") as file:
    file.write(formatted_headers)

