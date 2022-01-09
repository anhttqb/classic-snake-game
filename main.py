'''
Breaking the game into smaller part
1. Create a snake body
2. Move the snake
3. Control the snake
4. Detect when the snake hit the food
5. Create a score board
6. Detect collision with wall
7. Detect collision with tail
'''

from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") # set background color
screen.title("Snake Game")
# turn off the tracer
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

# using turtle listener to receive the command of the user to move the snake with 4 directions up, left, down, right
screen.listen()


screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score_board.get_score()
        snake.body_extend()
        snake.body_style()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]: # loop through the body's snake except the head
        # if snake's head collides with any segment in the tail.
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()













screen.exitonclick()