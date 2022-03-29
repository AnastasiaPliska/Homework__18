def check_mail(mail):
    if "@" in mail and "." in mail:
        return True
    else:
        return False


# print(check_mail("local@skypro"))
# print(check_mail("you(at)sky.pro"))
# print(check_mail("me@sky.pro"))
# print(check_mail("@lizaveta"))
# print(check_mail("alarm@gmail.com"))