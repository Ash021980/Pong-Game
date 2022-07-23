from turtle import Turtle


class Scoreboard(Turtle):
    """ Creates the scoreboard and keeps track of each player's score."""

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def __str__(self) -> str:
        return "Scoreboard for the game."

    def update_scoreboard(self) -> None:
        """ Updates the scoreboard when a player scores."""
        self.clear()
        self.goto(-50, 245)
        self.write(self.l_score, align="center", font=("Courier", 40, "bold"))
        self.goto(50, 245)
        self.write(self.r_score, align="center", font=("Courier", 40, "bold"))

    def l_point(self) -> None:
        """ Keeps track of the left player's score."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self) -> None:
        """ Keeps track of the right player's score."""
        self.r_score += 1
        self.update_scoreboard()

    def get_winner(self, winner: str) -> None:
        """ Notifies the players as to who the winner is. """
        self.color("red")
        self.goto(0, 0)
        self.write(f"{winner} wins the game!", move=False, align="center", font=("Courier", 20, "bold"))
