from question_model import Question


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
            print(f"Score: {self.score}/{self.question_number}")
        elif user_answer.lower() != "true" and user_answer.lower() != "false":
            print("Invalid input. Please enter 'True' or 'False'.")
            self.question_number -= 1
        else:
            print(f"Sorry, that's wrong. The correct answer was: {correct_answer}...")
            print(f"Score: {self.score}/{self.question_number}")
        print()
