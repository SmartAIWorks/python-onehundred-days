from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.render_score()

    def render_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font = FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font = FONT)
    def increment_score(self):
        self.score += 1
        self.render_score()