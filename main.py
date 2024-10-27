from snake import Snake
from snake_screen import SnakeScreen
from food import Food
from scoreboard import ScoreBoard


def map_snake_moves(screen: SnakeScreen, snake: Snake):
    """ Map keystrokes that listened by SnakeScreen to methods in Snake class. """
    keystrokes = {
        "Up": snake.move_up,
        "Down": snake.move_down,
        "Left": snake.move_left,
        "Right": snake.move_right,
    }
    for key, fun in keystrokes.items():
        screen.listen_to_keys(key, fun)


def collision_occours(snake: Snake):
    """ Detect collision with wall or with snake's own tail. Returns True
    if there is a collision, else returns False. """
    # Check for collision with the wall (x and y co-ordinates -280 to 280).
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        return True
    # Check for collision with snake's own tail.
    for snake_part in snake.snake_parts[1:]:
        if snake.head.distance(snake_part) < 10:
            return True
    return False


def main():
    """ Main method for the snake game.  """
    game_is_on = True
    screen = SnakeScreen()
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    map_snake_moves(screen, snake)

    while game_is_on:
        screen.update_screen()
        snake.move_snake()

        # Detect when snake reaches food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()

        # Detect collision with wall or with snake's own tail
        if collision_occours(snake): 
            scoreboard.reset()
            snake.reset()

    screen.exit_screen_on_click()


if __name__ == "__main__":
    main()
