from turtle import Turtle
from time import sleep


t = Turtle()
t.speed(50)

length_line = 100

for i in range(1, 6):
    t.forward(length_line)
    if i > 2:
        t.right(90)
    else:
        t.left(90)
        

sleep(2)
t.reset()


def decart_plane() -> None:
    t.speed(50)
    t.forward(200)
    t.left(180)
    t.forward(400)
    t.left(180)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(180)
    t.forward(400)


def first_circle(t: Turtle) -> None:
    t.speed(50)
    t.color("red")
    t.penup()
    t.goto(100, 100)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def second_square(t: Turtle) -> None:
    t.color("green")
    t.penup()
    t.home()
    t.goto(-150, 150)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()

def third_fiveangle(t: Turtle) -> None:
    # прямоугольник отрисовывать неинтересн,
    # по структуре это тот же квадрат
    # поэтому отрисуем пятиугольник
    t.speed(50)
    t.color("blue")
    t.penup()
    t.home()
    t.goto(-150, -150)
    t.begin_fill()
    for i in range(5):
        t.forward(50)
        t.left(60)
    t.end_fill()

def fourth_threangle(t: Turtle) -> None:
    t.speed(50)
    t.color("yellow")
    t.penup()
    t.home()
    t.goto(150, -150)
    t.begin_fill()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

decart_plane()
first_circle(t)
second_square(t)
third_fiveangle(t)
fourth_threangle(t)

t.screen.exitonclick()
