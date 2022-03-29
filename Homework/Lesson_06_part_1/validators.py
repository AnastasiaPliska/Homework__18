def check_pin(pin):

    if pin == "1234" or len(pin) != 4 or pin[0] == pin[1] == pin[2] == pin[3]:
        return False
    else:
        return True


def check_pass(password):
    letter = False
    num = False
    for i in password:
        if i.isalpha() == True:
            letter = True
        elif i.isdigit() == True:
            num = True
    if len(password)>=8 and letter and num:
        return True
    else:
        return False



def check_mail(mail):
    if "@" in mail and "." in mail:
        return True
    else:
        return False


def check_name(name):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    name_ = True

    for i in name:
        if i.lower() not in alphabet:
            name_ = False
    return name_


# check_pin()
# check_pass()
# check_mail()
# check_name()
