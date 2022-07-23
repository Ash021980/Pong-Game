from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net
import time

GAME_OVER = 7

# Set up basic game screen
screen = Screen()
screen.bgcolor('green')
screen.title("My Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Put a net in the center of the screen.
net = Net()
net.draw_net()

# Create the two paddle objects.
paddle_r = Paddle((372, 0))
paddle_l = Paddle((-380, 0))

# Create the ball object.
ball = Ball()

# Create the Scoreboard
scoreboard = Scoreboard()

# Set up the key commands for the players to move their paddle.
screen.listen()
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall.
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with the paddles.
    if ball.distance(paddle_r) < 50 and ball.xcor() > 345 or ball.distance(paddle_l) < 50 and ball.xcor() < -355:
        ball.bounce_x()

    # Detect win the ball passes the right paddle.
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when the ball passes the left paddle.
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

    # Get the winner
    if scoreboard.l_score == GAME_OVER:
        winner = "Player 1"
        scoreboard.get_winner(winner)
        game_on = False
    elif scoreboard.r_score == GAME_OVER:
        winner = "Player 2"
        scoreboard.get_winner(winner)
        game_on = False


screen.exitonclick()
