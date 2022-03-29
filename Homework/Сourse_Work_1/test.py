first_player = "rg"
second_player = "rgh"
first_score = 10
second_score = 2

def results():
    print(f"Игра окончена\n======\nИгрок 1 {first_player} - {first_score}\nИгрок 2 {second_player} - {second_score}\n======")
    if first_score == second_score:
        print("Ничья! Вы заработали одинаковое количество баллов.")
    elif first_score == second_score:
        print(f"Победил игрок 1 - {first_player}")
    else:
        print(f"Победил игрок 2 - {second_player}")
    print("======\nДанные записаны в файл")

results()