THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__ (self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text=f'Score {self.quiz.score}: ', fg='white', bg=THEME_COLOR)

        self.score_label.grid(row=0, column=1, columnspan=2)

        self.canvas= Canvas(width=300, height=250, bg='white')
        self.question_label = self.canvas.create_text(
            150,
            125, 
            width=280,
            text='Some questions here', 
            font=('Arial', 18, 'italic'), 
            fill=THEME_COLOR)
        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def true_pressed(self):
        is_correct = self.quiz.check_answer('True')
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer('False')
        self.give_feedback(is_correct)

    def update_score(self):
        self.score_label.config(text=f'Score {self.quiz.score}: ')

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_label, fill=THEME_COLOR)

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=question_text)
            self.update_score()
        else:
            self.canvas.itemconfig(self.question_label, text='No current question available.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def give_feedback(self, is_correct):
        self.canvas.itemconfig(self.question_label, fill='white')
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

