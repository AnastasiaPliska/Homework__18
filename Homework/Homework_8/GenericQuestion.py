class GenericQuestion:
    def __init__(self, question_text, author, complexity, correct_answer, theme, question_asked=False, user_answer="", is_right=True):
        self.question_text = question_text
        self.author = author
        self.complexity = complexity
        self.correct_answer = correct_answer
        self.theme = theme
        self.question_asked = question_asked
        self.user_answer = user_answer
        self.scores = complexity * 10
        self.is_right = is_right

    def __repr__(self):
        return self.question_text

class Question(GenericQuestion):
    def get_points(self):
        return int(self.scores)

    def is_correct(self):
        return self.user_answer in self.correct_answer

    def build_question(self):
        return f"Тема: {self.theme}. Cложность: {self.complexity}\nВопрос: {self.question_text}"
