from validators import check_pin, check_pass, check_mail, check_name


print(check_pin("1239"))
print(check_pin("3333"))
print(check_pin("1234"))
print(check_pin("00011"))
print(check_pin("8765"))


print(check_pass("secretd00r"))
print(check_pass("huskyeye5"))
print(check_pass("secret"))
print(check_pass("m3wm3wm3w"))
print(check_pass("fh43j_!"))


print(check_mail("local@skypro"))
print(check_mail("you(at)sky.pro"))
print(check_mail("me@sky.pro"))
print(check_mail("@lizaveta"))
print(check_mail("alarm@gmail.com"))


print(check_name("Данил"))
print(check_name("Р_и_т_а"))
print(check_name("К0нстантин"))
print(check_name("А Ф"))
print(check_name("Елена"))