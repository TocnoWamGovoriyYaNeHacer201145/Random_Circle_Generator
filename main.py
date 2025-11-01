from turtle import *
from random import *
mode = input(f'Enter mode random/custom:\n>>> ')
while True:
    if mode in ['r','random','c','custom']:
        if mode in ['custom','c']:
            turtle_color = input('Enter turtle color:')
            lr_settings = int(input('Enter maximum value for left and right:'))
            fb_settings = int(input('Enter maximum value for forward and backward:'))
            # Turtle settings
            color(turtle_color)
            speed(1000)
            home()
            hideturtle()
            # Random settings
            f, l, r, b = randrange(-80, fb_settings), randrange(-360, lr_settings), randrange(-80, fb_settings), randrange(-80, fb_settings)
            rrange = randint(10000, 1000000)
            for i in range(rrange):
                forward(f)
                left(l)
                right(r)
                backward(b)
        elif mode in ['random','r']:
            # Turtle settings
            color("black")
            speed(1000)
            home()
            hideturtle()
            # Random settings
            f, l, r, b = randrange(-80, 100), randrange(-360, 360), randrange(-360, 360), randrange(-80, 100)
            rrange = randint(10000, 1000000)
            for i in range(rrange):
                forward(f)
                left(l)
                right(r)
                backward(b)
        exitonclick()
    elif mode not in ['r','random','c','custom']:
        print('This mode does not exists, select one that exists!\n1. Random - r or random\n2. Custom - c or custom')
        mode = input('Enter mode:')
