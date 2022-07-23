from turtle import Turtle


class Paddle(Turtle):
    """ Creates the paddle super class and sets size and color.
        Sets the movement of the paddles on a given key press.
        Takes the positional argument as a tuple.
    """

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def move_up(self):
        """ Allows the player to move the paddle up."""
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), 250)

    def move_down(self):
        """ Allows the player to move the paddle down."""
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -250)
