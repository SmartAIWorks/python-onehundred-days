from question_model import Question
from typing import List, Optional

class QuizBrain:

    def __init__(self, q_list: List[Question]):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question: Optional[Question] = None


    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        #user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")

        
        #self.check_answer(user_answer)

        return f"Q.{self.question_number}: {self.current_question.text} (True/False): "

    def check_answer(self, user_answer: str):
        if self.current_question is None:
            print("No current question available.")
            return False
        
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            
            return True
    
        return False
        # else:
        #     print("That's wrong.")

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
