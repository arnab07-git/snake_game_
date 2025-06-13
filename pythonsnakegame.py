import turtle as turt
import random
import time

DELAY = 0.12
score = 0
high_score = 0

screen = turt.Screen()
screen.title("🐍 Snake Game 🐍")
screen.bgcolor("#1a1a1a")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turt.Turtle()
head.shape("square")
head.color("#00ff00")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = turt.Turtle()
food.speed(0)
food.shape(random.choice(['circle']))  #
food.color("#ff3366")
food.penup()
food.goto(0, 100)

# Score card display korar jonno!!!
pen = turt.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#ffffff")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))


def up():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def left():
    if head.direction != "right":
        head.direction = "left"


def right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


screen.listen()
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

segments = []

while True:
    screen.update()

    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        food.goto(random.randint(-270, 270), random.randint(-270, 270))

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        DELAY = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Arial", 24, "bold"))

    if head.distance(food) < 20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))

        new_segment = turt.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        color_value = len(segments) * 20 % 255
        new_segment.color(f"#{color_value:02x}ff00")
        new_segment.penup()
        segments.append(new_segment)

        DELAY *= 0.95  # For Improvised speed!!!
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Arial", 24, "bold"))

    for i in range(len(segments) - 1, 0, -1):
        x, y = segments[i - 1].xcor(), segments[i - 1].ycor()
        segments[i].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision checking code part:-
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            food.goto(random.randint(-270, 270), random.randint(-270, 270))

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            DELAY = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center", font=("Arial", 24, "bold"))

    time.sleep(DELAY)