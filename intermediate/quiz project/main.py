from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'],question['correct_answer']))

quiz = QuizBrain(question_bank)
score = 0
while not quiz.at_end():
    quiz.is_correct(quiz.next_question())

