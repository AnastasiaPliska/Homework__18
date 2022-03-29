def check_name(name):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    name_ = True

    for i in name:
        if i.lower() not in alphabet:
            name_ = False
    return name_


# print(check_name("Данил"))
# print(check_name("Р_и_т_а"))
# print(check_name("К0нстантин"))
# print(check_name("А Ф"))
# print(check_name("Елена"))
