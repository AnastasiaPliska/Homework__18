import json

with open('questions.json', "r+", encoding="utf-8") as file:
    questions = json.load(file)


def play_field(questions):
    print("")
    for category in questions.keys():
        scores = [str(score) if questions[category][score]["asked"] == True else " " for score in questions[category].keys()]
        print(f"{category.ljust(13)}", end="")
        for points in scores:
            print(f"{points.ljust(7)}", end="")
        print()


points = 0
correct = 0
incorrect = 0

while True:
    play_field(questions)
    user_choice = input("Выберите категорию ")

    if len(user_choice.split()) != 2:
        print("Ошибка ввода")
        break
    category, score = user_choice.split()

    if category in questions.keys():
        if score in questions[category].keys():
            if questions[category][score]["asked"] == False:
                print("Этот вопрос уже задан, попробуйте еще раз!")
                continue
            else:
                questions[category][score]["asked"] = False
                print(f'Слово {questions[category][score]["question"]} в переводе означает:')
                answer = input().lower()
                if answer == questions[category][score]["answer"]:
                    points += int(score)
                    correct += 1
                    print(f"Верно, + {score}. Ваш счет = {points}")
                else:
                    points -= int(score)
                    incorrect += 1
                    print(f'Неверно, на самом деле - {questions[category][score]["answer"]}. - {score}. Ваш счет = {points}')
        else:
            print("Такого вопроса нет, попробуйте еще раз!")
    else:
        print("Данная категория отсутствует, попробуйте еще раз!")


    is_game = []
    for category in questions.keys():
        for score in questions[category].keys():
            is_game.append(questions[category][score]["asked"])
    if sum(is_game) == 0:
        print(f'У нас закончились вопросы!\nВаш счет: {points}\nВерных ответов: {correct}\nНеверных ответов: {incorrect}')
        break


with open('results.json', "w") as file:
    result = {
        'points': points,
        'correct': correct,
        'incorrect': incorrect
    }
    file.write(json.dumps(result))
