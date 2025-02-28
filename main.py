from turtle import *
import turtle
from random import *
mode = input('Enter mode (random/custom): ')
if mode == 'custom':
    lr_settings = int(input('Enter maximum left and right value: '))
    fb_settings = int(input('Enter maximum forward and backward value: '))
    # Turtle setup
    turtle.color("black")
    turtle.speed(0)
    turtle.home()
    hideturtle()
    # Random forward and left movement setup
    f, l, r, b = randrange(-80, fb_settings), randrange(-360, lr_settings), randrange(-80, fb_settings), randrange(-80, fb_settings)
    rrange = randint(10000, 1000000)
    for i in range(rrange):
        forward(f)
        left(l)
        right(r)
        backward(b)
elif mode == 'random':
    # Turtle setup
    turtle.color("black")
    turtle.speed(0)
    turtle.home()
    hideturtle()
    # Random forward and left movement setup
    f = randrange(-80, 100)
    l = randrange(-360, 360)
    r = randrange(-360, 360)
    b = randrange(-80, 100)
    rrange = randint(10000, 1000000)
    for i in range(rrange):
        forward(f)
        left(l)
        right(r)
        backward(b)
exitonclick()
