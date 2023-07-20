# We are not using Turtle class in main.py as it is used to create Snake, Food and Scoreboard classes
# in their respective files.

from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
from gameover import Gameover


screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

score_count = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect the collision with food and food moves to another random location and the scoreboard gets maintained
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.extend()
        score.increase_score()

    #Detect collision with the wall and end the game
    elif snake.head.xcor() < -320 or snake.head.xcor() > 320 or snake.head.ycor() < -277 or snake.head.ycor() > 277:
        # game_is_on = False
        # game_over = Gameover()
        # Now we are not ending the game. Rather we are updating the high score at the end of each game and the game
        # continues to run indefinitely.
        score.reset()
        snake.reset()


    #Detect collision with snake's body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            #Now we are not ending the game. Rather we are updating the high score at the end of each game and the game
            #continues to run indefinitely.
            # game_is_on = False
            # game_over = Gameover()



screen.exitonclick()
