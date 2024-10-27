from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self._create_snake()
        self.head = self.snake_parts[0]

    def _create_snake(self):
        """ Create snake body of 3 squares and of color white. Set position
        of each of the snake parts. """
        for position in STARTING_POSITIONS:
            self._add_a_snake_part(position)

    def _add_a_snake_part(self, position):
        """ Add another part or segment to snake. """
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def extend_snake(self):
        """ Extend snake by adding another part to the end of the snake. """
        self._add_a_snake_part(self.snake_parts[-1].position())

    def move_snake(self):
        """ Move snake to the next position by moving each individual parts of snake. """
        for part_index in range(len(self.snake_parts) - 1, 0, -1):
            x, y = self.snake_parts[part_index - 1].position()
            self.snake_parts[part_index].goto(x, y)
        self.head.forward(20)

    def move_up(self):
        """ Move snake up by changing the direction of snake head to 90 degrees,
        if not moving down to prevent the snake from going in reverse direction. """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """ Move snake down by changing the direction of snake head to 270 degrees,
        if not moving up to prevent the snake from going in reverse direction. """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        """ Move snake left by changing the direction of snake head to 180 degrees,
        if not moving right to prevent the snake from going in reverse direction. """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        """ Move snake right by changing the direction of snake head to 0 degrees,
        if not moving left to prevent the snake from going in reverse direction. """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """ Reset the snake by moving the current snake parts away from screen.
        Creating a new snake and setting the snake head to the first snake part. """
        for snake_part in self.snake_parts:
            snake_part.goto(1000, 1000)
        self.snake_parts.clear()
        self._create_snake()
        self.head = self.snake_parts[0]
