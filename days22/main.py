from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


paddle_r = Paddle((380, 0))
paddle_l = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')


screen.onkey(paddle_l.go_up, 'w')
screen.onkey(paddle_l.go_down, 's')


is_game_on = True
while(is_game_on):
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    # Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with the paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    # Bounce if the paddle saves the ball
    if ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Score left paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    # Score right paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()


