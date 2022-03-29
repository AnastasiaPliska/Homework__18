def check_pin(pin):

    if pin == "1234" or len(pin) != 4 or pin[0] == pin[1] == pin[2] == pin[3]:
        return False
    else:
        return True


# print(check_pin("1239"))
# print(check_pin("3333"))
# print(check_pin("1234"))
# print(check_pin("00011"))
# print(check_pin("8765"))
