
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
    
        self.l_score = 0
        self.r_score = 0

        self.render_score()

    def r_point(self):
        self.r_score += 1
        self.render_score()

    def l_point(self):
        self.l_score += 1
        self.render_score()

    def render_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align='center', font=('Arial', 75, 'normal'))

        self.goto(100, 200)
        self.write(f"{self.r_score}", align='center', font=('Arial', 75, 'normal'))
 
