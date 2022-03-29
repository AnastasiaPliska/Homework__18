virus_code = "Я вирус"

with open('answers.py', encoding="utf-8") as file:
    content = file.read()

    if virus_code in content:
        print("Вирус обнаружен")
    else:
        print("Всё хорошо, вирусов нет")