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
    return turtle

def draw_circle(turtle, radius, step_angle):
    for _ in range(int(360 / step_angle)):
        turtle.color(random.choice(colors))
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + step_angle)

def draw_square(turtle, side_length, step_angle):
    for _ in range(int(360 / step_angle)):
        turtle.color(random.choice(colors))
        for _ in range(4):
            turtle.forward(side_length)
            turtle.right(90)
        turtle.setheading(turtle.heading() + step_angle)

def draw_spirograph(turtle, shape, size, step_angle):
    if shape == "circle":
        draw_circle(turtle, size, step_angle)
    elif shape == "square":
        draw_square(turtle, size, step_angle)

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

screen = setup_screen()
turtle = setup_turtle()

draw_spirograph(turtle, "circle", 100, 10)

turtle.clear()

draw_spirograph(turtle, "square", 100, 10)

screen.exitonclick()