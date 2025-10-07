#from turtle import Turtle, Screen
#import turtle as T
# Basic import turtle turtle.Turtle
# from import - from turtle import Turtle
# * - from turtle import *
# alias - import tutle as t - t.Turtle()
# installing modules




# tim = Turtle()
# tim.shape('turtle')

# tim.color('red', 'green')

# for _ in range(4):
#     tim.forward(200)
#     tim.right(90)


# import random

# colors = [
#     "red",
#     "blue",
#     "green",
#     "yellow",
#     "orange",
#     "purple",
#     "pink",
#     "brown",
#     "black",
#     "white",
#     "gray",
#     "cyan",
#     "magenta",
#     "lime",
#     "teal",
#     "navy",
#     "maroon",
#     "olive",
#     "silver",
#     "gold"
# ]

# angles = [0, 90, 180, 270]
# color_numbers = [0, 255]
# tim = Turtle()
# #T.colormode(255)
# tim.pensize(20)
# tim.speed(20)

# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(angles))

# screen = Screen()
# screen.exitonclick()



import colorgram

def get_colors_from_image():
    colors = colorgram.extract('./day18/image.jpg', 30)
    rgb = []
    for color in colors:
        rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb