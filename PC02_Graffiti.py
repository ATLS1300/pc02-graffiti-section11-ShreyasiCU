#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:28:26 2021

@author: shreyasimandal
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on.
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on.
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

# Circle Code
turtle.speed(0)
turtle.up()
turtle.goto(-20,-10)
turtle.down()
turtle.circle(130)

# Polygon Code ( Making 3 star shapes of different line widths )
turtle.up()


for b in range(0,3):
    turtle.goto(-100+(b*80),350)
    turtle.down()
    turtle.pensize(2*b)
    for a in range(0,5):
        turtle.fd(50)
        turtle.rt(2*360/5)
       
    turtle.up()

# Line
   
turtle.goto(-130,300)
turtle.down()
turtle.fd(280)

#circle

turtle.penup()
turtle.goto(0, -363)
turtle.bgcolor("grey")
turtle.color("magenta", "cyan")

turtle.pendown()
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()


turtle.hideturtle()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()