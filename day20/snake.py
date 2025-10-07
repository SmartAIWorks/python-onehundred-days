
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        segments = []
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)
        
        self.segments = segments


    def move(self):

        segments = self.segments
        for seg_num in range(len(segments) -1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()

            segments[seg_num].goto(new_x, new_y)
        
        segments[0].forward(20)
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)