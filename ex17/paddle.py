from turtle import Turtle

class Paddle:
    def __init__(self, x, y):
        self.paddle = Turtle()
        self.paddle.color("#00FF00")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)
        self.move_up_pressed = False
        self.move_down_pressed = False

    def move_up(self):
        if self.paddle.ycor() < 350:
            self.paddle.sety(self.paddle.ycor() + 15)

    def move_down(self):
        if self.paddle.ycor() > -350:
            self.paddle.sety(self.paddle.ycor() - 15)

    def start_moving_up(self):
        self.move_up_pressed = True

    def start_moving_down(self):
        self.move_down_pressed = True

    def stop_moving_up(self):
        self.move_up_pressed = False

    def stop_moving_down(self):
        self.move_down_pressed = False

    def update(self):
        if self.move_up_pressed:
            self.move_up()
        if self.move_down_pressed:
            self.move_down()
