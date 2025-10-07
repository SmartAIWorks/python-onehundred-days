from turtle import Screen, Terminator
from tkinter import TclError
import time

from snake import Snake


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
        except (Terminator, TclError):
            # Window closed while loop was running; end the game loop cleanly
            is_game_on = False
            break




if __name__ == '__main__':
    main()