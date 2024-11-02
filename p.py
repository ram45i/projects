import turtle 
import time
import random

delay = 0.4

# Screen setup
sc = turtle.Screen()
sc.bgcolor("red")
sc.title("Snake_Game")
sc.setup(width=600, height=600)
sc.tracer(0)

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0, 200)

segments = []

# Functions to control the snake
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
sc.listen()
sc.onkeypress(go_up, "w")
sc.onkeypress(go_down, "s")
sc.onkeypress(go_left, "a")
sc.onkeypress(go_right, "d")

# Main game loop
while True:
    sc.update()
    
    # Check for a collision with the border
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"
        # Optionally, you can reset segments here
        segments.clear()  # Clear segments on collision

    # Check for a collision with the food
    if snake.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()    

sc.mainloop()

