

class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        ''' Check if there are still questions to be asked. '''
        return self.question_no < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        ''' Check if the user answer is correct. '''
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('That is wrong!')
        
        print(f'The correct answer was {correct_answer}')
        print(f"Your current score is {self.score}/{self.question_no}")

    def next_question(self):
        ''' Generates the next question '''
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"Q{self.question_no} : {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)
    
