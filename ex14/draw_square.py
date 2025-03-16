from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("white")
t.speed(1)
s = Screen()
s.title("Square Drawing")
s.bgcolor("black")
s.setup(width=600, height=600)
t.setheading(90)
for _ in range(4):
	t.forward(100)
	t.right(90)
s.exitonclick()

