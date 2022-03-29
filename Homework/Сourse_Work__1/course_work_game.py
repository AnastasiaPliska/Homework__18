import requests
import random
import json

response = requests.get('https://jsonkeeper.com/b/JHXA')
response_json = response.json()
random.shuffle(response_json)
word = response_json[0]

first_player = ""
second_player = ""
first_score = 0
second_score = 0
words = []

print("Добро пожаловать в игру!")

while True:
    if len(first_player) == 0:
        first_player = (input("Введите имя первого игрока\n")).title()
    if len(second_player) == 0 or second_player == first_player:
        second_player = (input("Введите имя второго игрока\n")).title()
    else:
        break

print(f"{first_player.upper()} vs {second_player.upper()}, игра начинается!")
print(f"Ваше слово на эту игру:\n{word.upper()}")

while True:
    print(f"======\nНачало раунда.\n{word.upper()}\nХодит игрок {first_player.upper()}")
    first_word = input().lower()
    word_one = word
    first_r_score = 0
    if first_word == "stop":
        break
    elif first_word in words:
        print("Такое слово уже было.")
    else:
        for letter in first_word:
            if letter in word_one:
                word_one = word_one.replace(letter, ".", 1)
                first_r_score += 1
                if first_r_score == len(first_word):
                    words.append(first_word)
                    first_score += first_r_score
                    print("Принято")
            else:
                print("Нет такого слова.")

    print(f"Ходит игрок {second_player.upper()}")
    second_word = input().lower()
    word_two = word
    second_r_score = 0
    if second_word == "stop":
        break
    elif second_word in words:
        print("Такое слово уже было.")
    else:
        for letter in second_word:
            if letter in word_two:
                word_two = word_two.replace(letter, ".", 1)
                second_r_score += 1
                if second_r_score == len(second_word):
                    words.append(second_word)
                    second_score += second_r_score
                    print("Принято")
            else:
                print("Нет такого слова.")


def results():
    print(
        f"======\nИгра окончена\n======\nИгрок 1 {first_player} - {first_score}\nИгрок 2 {second_player} - {second_score}\n======")
    if first_score == second_score:
        print("Ничья! Вы заработали одинаковое количество баллов.")
    elif first_score > second_score:
        print(f"Победил игрок 1 - {first_player}")
    else:
        print(f"Победил игрок 2 - {second_player}")
    print("======\nДанные записаны в файл")


results()


with open("results.json", "w", encoding="utf-8") as file:
    result = {
        'users': {
            '1': first_player,
            '2': second_player
        },
        'word': word,
        'words': words
    }
    file.write(json.dumps(result))
