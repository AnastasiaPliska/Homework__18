import json
import random
from GenericQuestion import Question


def read_question(filename):
    question_list = []

    with open(filename, "r", encoding="utf-8") as file:
        question_dict = json.load(file)

    for key in question_dict.keys():
        question_list.append(Question(
            question_text=key,
            author=question_dict[key]["author"],
            complexity=question_dict[key]["complexity"],
            correct_answer=question_dict[key]["correct_answer"],
            theme=question_dict[key]["theme"]
        ))

    return question_list


questions = read_question("question.json")
random.shuffle(questions)

for question in questions:
    print(f"Вопрос: {questions.index(question) + 1}. Сложность: {question.complexity}/5. Тема: {question.theme}. Автор вопроса: {question.author}.")
    print(question)

    user_answer = input()

    question.user_answer = user_answer
    question.question_asked = True

    if question.user_answer in question.correct_answer:
        print(f"Ответ верный, получено {question.scores} баллов")
        question.is_right = True
    else:
        print(f"Ответ неверный. Верный ответ – {question.correct_answer[0]}")
        question.is_right = False


def statistics(question_list):
    result_game = {
        "total_questions": 0,
        "right_answers": 0,
        "total_score": 0,
    }

    for question in question_list:
        if question.question_asked:
            result_game["total_questions"] += 1
            if question.is_right:
                result_game["total_score"] += question.scores
                result_game["right_answers"] += 1

    return result_game


result_game = statistics(questions)

print(f'Вот и всё!\nОтвечено {result_game["right_answers"]} вопросов из {result_game["total_questions"]}')
