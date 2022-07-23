from turtle import Turtle


class Net(Turtle):
    """ Places a net in the middle of the screen. """

    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.setheading(270)
        self.width(5)

    def draw_net(self):
        """ Draws the net on screen. """
        for _ in range(30):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
