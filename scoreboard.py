from turtle import Turtle
import os


ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')
HIGHSCORE_FILE = "data.txt"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        self.highscore_filepath = None
        self._set_highscore_filepath()
        self._get_highscore()
        self._update_scoreboard()

    def _set_highscore_filepath(self):
        """ Set filepath of HIGHSCORE_FILE. """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.highscore_filepath = os.path.join(current_dir, HIGHSCORE_FILE)

    def _get_highscore(self):
        """ Read previous high score from HIGHSCORE_FILE. """
        with open(self.highscore_filepath, "r") as file:
            data = file.read()
            if data:
                self.high_score = int(data.strip())

    def _set_high_score(self):
        """ Write high score to HIGHSCORE_FILE. """
        with open(self.highscore_filepath, "w") as file:
            file.write(str(self.high_score))

    def _update_scoreboard(self):
        """ Update the scoreboard. """
        self.clear()
        msg = f"Score: {self.score}  High Score: {self.high_score}"
        self.write(msg, move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ Increase the score by value of 1. """
        self.score += 1
        self._update_scoreboard()

    def reset(self):
        """ Reset score board. Update  score and high score. """
        if self.score > self.high_score:
            self.high_score = self.score
            self._set_high_score()
        self.score = 0
        self._update_scoreboard()

