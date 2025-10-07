from turtle import Screen, Terminator
from tkinter import TclError

from food import Food
from snake import Snake
from score import Score

import time



def initialize_screen():
    screen = Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor('black')
    screen.title('My Snake Game!')
    screen.tracer(0)
    return screen

def main():

    screen = initialize_screen()


    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    is_game_on = True

    while is_game_on:
        try:
            screen.update()
            time.sleep(0.1)
            snake.move()

            if snake.head.distance(food) < 15:
                score.increment_score()
                food.reset()
                snake.extend()
            
            # Detect collisions with wall
            if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
                is_game_on = False
                score.game_over()
            
            # Detect self collisions
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 15:
                    is_game_on = False
                    score.game_over()

            
        except (Terminator, TclError):
            # Window closed while loop was running; end the game loop cleanly
            is_game_on = False
            return

    screen.exitonclick()


if __name__ == '__main__':
    main()