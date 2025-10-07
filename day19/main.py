from turtle import Turtle, Screen

def free_draw():
    tim = Turtle()
    screen = Screen()

    def move_forwards():
        tim.forward(10)

    def move_backwards():
        tim.backward(10)

    def turn_left():
        tim.left(10)

    def turn_right():
        tim.right(10)

    def clear():
        tim.clear()
        tim.penup()
        tim.home()
        tim.pendown()

    screen.listen()
    screen.onkey(move_forwards, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear, "c")

    screen.exitonclick()


def start_race():
    pass

def turtle_race():
    screen = Screen()
    screen.setup(height=400, width=500)

    colors = ['red', 'yellow', 'green', 'blue']

    turtles: list[Turtle] = []

    for color in colors:
        tur = Turtle(shape='turtle')
        tur.color(color)
        turtles.append(tur)


    y = -100

    for t in turtles:
        y += 50
        t.penup()
        t.goto(x=-230, y=y)

    screen.exitonclick()

def main():
    #free_draw();
    turtle_race()


if __name__ == '__main__':
    main()