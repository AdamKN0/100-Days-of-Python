from turtle import Turtle, Screen
from random import randint

s = Screen()

turtles = []
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
for i in range(8):
    t = Turtle()
    t.speed("fastest")
    t.pensize(5)
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-300, 200 - i * 50)
    turtles.append(t)

finish_line = 300
winner = None

while not winner:
    for t in turtles:
        t.forward(randint(1, 10))
        if t.xcor() >= finish_line:
            winner = t
            break

s.clearscreen()

winner_turtle = Turtle()
winner_turtle.hideturtle()
winner_turtle.penup()
winner_turtle.goto(0, 0)
winner_turtle.write(f"The winner is the {winner.color()[0]} turtle!", align="center", font=("Arial", 24, "normal"))

s.exitonclick()