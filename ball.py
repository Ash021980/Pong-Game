from turtle import Turtle


class Ball(Turtle):
    """ Creates the ball object and initiates its movement. """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """ Moves the ball across the screen. """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Reverses the direction of the ball when it touches the top or bottom boundary. """
        self.y_move *= -1

    def bounce_x(self):
        """ Reverses the direction of the ball when it touches one of the paddles. """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """ Resets the ball position to the center of the screen and change the direction. """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
