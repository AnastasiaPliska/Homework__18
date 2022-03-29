import random

user_name = input("Введите ваше имя ")
scores = 0


def read_words():
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


read_words()

with open('history.txt', 'a', encoding="utf-8") as file:
    file.write(f"{user_name} {scores}\n")


# def user_list(user_name, scores):
#     # with open('history.txt', 'a', encoding="utf-8") as file:
#     #     file.write(f"{user_name} {scores}\n")
#     file_history = open('history.txt', 'a', encoding="utf-8")
#     file_history.write(f"{user_name} {scores}\n")
#     file_history.close()


def games_result():
    games = 0
    max_scores = 0
    with open('history.txt') as file:
        for gamer in file:
            if len(gamer.strip().split(' ')) == 2:
                user, user_scores = gamer.strip().split(' ')

                if int(user_scores.rstrip('\n')) > max_scores:
                    max_scores = int(user_scores)
            games += 1
    return games, max_scores


games, max_scores = games_result()
print(f'Всего игр сыграно: {games}\nМаксимальный рекорд: {max_scores}')
