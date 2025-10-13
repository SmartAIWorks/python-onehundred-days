from question_model import Question
from data import fetch_data
from quiz_brain import QuizBrain
from typing import Dict, List, Any
from ui import QuizInterface

data: List[Dict[str, Any]] = fetch_data()

question_bank = []
for question in data:
    question_text: str = question["question"]
    question_answer: str = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz_brain = QuizBrain(question_bank)
quiz = QuizInterface(quiz_brain)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
