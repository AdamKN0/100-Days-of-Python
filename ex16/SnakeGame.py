from turtle import Turtle, Screen
import time
import random

class SnakeGame:
    def __init__(self, food, score):
        self.snake_segments = []
        self.screen = self.setup_screen()
        self.food = food
        self.score = score
        self.game_is_on = True
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.setup_controls()

    def setup_screen(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        return screen

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()

    def move_snake(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        self.snake_segments[0].forward(20)

    def up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)

    def down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)

    def left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)

    def right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")
        self.screen.onkey(self.restart_game, "c")
        self.screen.onkey(self.quit_game, "q")

    def check_food_collision(self):
        if self.snake_segments[0].distance(self.food) < 15:
            self.food.refresh()
            self.add_segment(self.snake_segments[-1].position())
            self.score.increase_score()

    def check_wall_collision(self):
        head = self.snake_segments[0]
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            self.end_game()

    def check_self_collision(self):
        for segment in self.snake_segments[1:]:
            if self.snake_segments[0].distance(segment) < 10:
                self.end_game()

    def end_game(self):
        self.score.game_over()
        self.game_is_on = False

    def restart_game(self):
        self.score.reset()
        self.reset_snake()
        self.game_is_on = True
        self.run_game()

    def quit_game(self):
        self.screen.bye()

    def run_game(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.move_snake()
            self.check_food_collision()
            self.check_wall_collision()
            self.check_self_collision()
        self.screen.exitonclick()
