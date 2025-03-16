from turtle import Turtle, Screen
import random

def setup_screen():
    screen = Screen()
    screen.title("Epic Random Walk")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    return screen

def setup_turtle():
    turtle = Turtle()
    turtle.pensize(1)
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-280, 280)
    return turtle

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

def draw_dots(turtle):
    rows = 12
    cols = 12
    dot_size = 20
    spacing = 50
    for y in range(rows):
        for x in range(cols):
            turtle.dot(dot_size, random.choice(colors))
            turtle.forward(spacing)
        turtle.backward(spacing * cols)
        turtle.right(90)
        turtle.forward(spacing)
        turtle.left(90)

screen = setup_screen()
turtle = setup_turtle()

draw_dots(turtle)

screen.exitonclick()
