from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.lives = 3
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-300, 260)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 16, "bold"))
        self.goto(0, 260)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 16, "bold"))
        self.goto(300, 260)
        self.write(f"Lives: {self.lives}", align="right", font=("Arial", 16, "bold"))

    def increase_score(self):
        self.score += 5
        self.update_score()

    def increase_level(self):
        self.level += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Arial", 36, "bold"))