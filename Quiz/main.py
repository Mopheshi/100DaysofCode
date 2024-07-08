from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    # new_question = question["text"]
    # new_answer = question["answer"]
    new_question = question["question"]
    new_answer = question["correct_answer"]
    newQuestion = Question(new_question, new_answer)
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"You've scored: {quiz.score}/{quiz.question_number}")
