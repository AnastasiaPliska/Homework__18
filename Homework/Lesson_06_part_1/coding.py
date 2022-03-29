alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def shift_encode(string):
    encode_string = []
    for i in string:
        if i == "я":
            encode_string.append("а")
        else:
            encode_string.append(alphabet[alphabet.find(i) + 1])
    print("".join(encode_string))


shift_encode("ссср")


def shift_decode(string):
    decode_string = []
    for i in string:
        if i == "а":
            decode_string.append("я")
        else:
            decode_string.append(alphabet[alphabet.find(i) - 1])
    print("".join(decode_string))


shift_decode("тттс")