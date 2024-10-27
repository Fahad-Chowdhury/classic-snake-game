from turtle import Screen
import time

class SnakeScreen:

    def __init__(self):
        self.screen = Screen()
        self._setup_screen()

    def _setup_screen(self):
        """ Setup screen. """
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.screen.listen()

    def update_screen(self):
        """ Update snake on screen. """
        self.screen.update()
        time.sleep(0.2)

    def listen_to_keys(self, key, fun):
        """ Map keyboard stroke to snake move. """
        self.screen.onkey(key=key, fun=fun)

    def exit_screen_on_click(self):
        """ Close screen on mouseclick. """
        self.screen.exitonclick()
