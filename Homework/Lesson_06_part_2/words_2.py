import random

user_name = input("Введите ваше имя ")
scores = 0
games = 0
max_scores = 0


with open('words.txt') as file:
    for line in file:
        word = line.rstrip('\n')
        new_word = random.sample(word, (len(word)))

        print(f'Угадайте слово: {"".join(new_word)}')
        answer = input()
        if answer == word:
            scores += 10
            print("Верно! Вы получаете 10 очков.")
        else:
            print(f"Неверно! Верный ответ - {word}")

with open('history.txt', 'a', encoding="utf-8") as file:
    file.write(f"{user_name} {scores}\n")


with open('history.txt') as file:
    for gamer in file:
        user, user_scores = gamer.strip().split(' ')
        games += 1
        if int(user_scores.rstrip('\n')) > max_scores:
            max_scores = int(user_scores)

    print(f'Всего игр сыграно: {games}\nМаксимальный рекорд: {max_scores}')


