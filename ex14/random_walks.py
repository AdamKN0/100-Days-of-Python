from turtle import Turtle, Screen
import random

t = Turtle()
t.pensize(15)
s = Screen()
s.title("Epic Random Walk")
s.bgcolor("black")
s.setup(width=600, height=600)
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
angles = [0, 90, 180, 270]
t.speed("fastest")

for _ in range(200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(angles))
    if t.xcor() > 290 or t.xcor() < -290 or t.ycor() > 290 or t.ycor() < -290:
        t.right(180)

s.exitonclick()