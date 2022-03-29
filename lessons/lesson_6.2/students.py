# Драт Калмин учит язык python

with open("students.txt", encoding="utf-8") as file:
    for student_data in file:
        # # data = student_data.split(":")
        # data = student_data.rstrip('\n').split(":")
        #
        # name = data[0]
        # language = data[1]

        name, language = student_data.rstrip('\n').split(":")

        print(f"{name} учит язык {language}!")
