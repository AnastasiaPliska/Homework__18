dictionary = {
    "out": "Вы вышли из системы",
    "noaccess": "У вас нет доступа в этот раздел",
    "unknown": "Неизвестная ошибка",
    "timeout": "Система долго не отвечает",
    "robot": "Ваши действия похожи на робота",
}
list_errors = []

def get_errors(*errors):
    for error in errors:
        if error in dictionary:
            list_errors.append(dictionary[error])
        else:
            list_errors.append("Ошибка отсутствует")
    print(list_errors)


get_errors("out", "robot", "hello", "timeout", "unknown")
