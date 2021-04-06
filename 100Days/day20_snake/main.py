from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.screensize(600, 600)         # set screen size
screen.bgcolor("darkblue")
screen.title("Snaaaaaake!!!")
screen.tracer(0)        # setting tracer to 0 turns live turtle animations off, so the screen can be updated as determined

snake = Snake()         # refer to the Snake classes from snake
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_score = 0

game_on = True
while game_on:
    screen.update()        # as tracer is off, screen is updated within this function, with below delay of 0.1 seconds added.
    time.sleep(0.1)
    snake.move()            # run the move function from the snake variable, whish is from the Snake class

    # detect collision between snake & food
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        score.update_score()

screen.exitonclick()