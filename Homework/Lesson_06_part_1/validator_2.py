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

# print(check_pass("secretd00r"))
# print(check_pass("huskyeye5"))
# print(check_pass("secret"))
# print(check_pass("m3wm3wm3w"))
# print(check_pass("fh43j_!"))