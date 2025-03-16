from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_up():
    t.forward(10)

def move_down():
    t.backward(10)

def move_left():
    t.left(10)

def move_right():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(move_up, "Up")
s.onkey(move_down, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")
s.onkey(clear, "c")

s.exitonclick()
