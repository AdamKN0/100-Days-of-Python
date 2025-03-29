from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#000000")
screen.title("Epic Pong")
screen.tracer(0)

mode = None
while mode not in ["1", "2"]:
    mode = screen.textinput("Choose Mode", "1 = Play with Bot\n2 = Play with Friend")

paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.start_moving_up, "Up")
screen.onkeyrelease(paddle_right.stop_moving_up, "Up")
screen.onkeypress(paddle_right.start_moving_down, "Down")
screen.onkeyrelease(paddle_right.stop_moving_down, "Down")

if mode == "2":
    screen.onkeypress(paddle_left.start_moving_up, "z")
    screen.onkeyrelease(paddle_left.stop_moving_up, "z")
    screen.onkeypress(paddle_left.start_moving_down, "s")
    screen.onkeyrelease(paddle_left.stop_moving_down, "s")

def bot_move():
    if ball.ball.ycor() > paddle_left.paddle.ycor() + 10:
        paddle_left.move_up()
    elif ball.ball.ycor() < paddle_left.paddle.ycor() - 10:
        paddle_left.move_down()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.speed)

    ball.move()
    paddle_right.update()
    paddle_left.update()

    if ball.ball.distance(paddle_right.paddle) < 50 and ball.ball.xcor() > 340:
        ball.bounce_x()
    if ball.ball.distance(paddle_left.paddle) < 50 and ball.ball.xcor() < -340:
        ball.bounce_x()

    ball.check_wall_collision()

    if ball.ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_point()
    if ball.ball.xcor() < -390:
        ball.reset_position()
        scoreboard.right_point()

    if mode == "1":
        bot_move()

screen.exitonclick()
