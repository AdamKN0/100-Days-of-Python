from turtle import Turtle

class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("lime green")
        self.turtle.setheading(90)
        self.turtle.penup()
        self.reset_position()
        self.move_distance = 20

    def move_up(self):
        self.turtle.forward(self.move_distance)

    def reset_position(self):
        self.turtle.goto(0, -280)

    def is_at_finish_line(self):
        return self.turtle.ycor() > 280