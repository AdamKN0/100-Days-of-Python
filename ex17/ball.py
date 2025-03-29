from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.color("#FF0000")
        self.ball.shape("circle")
        self.ball.penup()
        self.reset_position()
    
    def reset_position(self):
        self.ball.goto(0, 0)
        self.x_move = 8
        self.y_move = 8
        self.speed = 0.02

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed *= 0.95

    def check_wall_collision(self):
        if self.ball.ycor() > 390 or self.ball.ycor() < -390:
            self.bounce_y()
