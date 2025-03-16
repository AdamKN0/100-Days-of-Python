from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.speed(1)
s = Screen()
s.title("Square Drawing")
s.bgcolor("black")
s.setup(width=600, height=600)
t.setheading(90)

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

def draw_shape(num_side, color):
    t.color(color)
    angle = 360 / num_side
    for _ in range(num_side):
        t.forward(100)
        t.right(angle)

color_index = 0
for sides in range(3, 11):
    draw_shape(sides, colors[color_index])
    color_index += 1
    if color_index >= len(colors):
        color_index = 0

s.exitonclick()