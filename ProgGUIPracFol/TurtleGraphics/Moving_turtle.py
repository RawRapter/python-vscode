"""
Creating randomly moving turtle.
"""

import turtle as t
import random as ri

#Creating def for Boundary so that it doesn't go out of the window
def inside_window():
    #reducing boundary from left side
    left_limit = (-t.window_width() / 2) + 100
    #reducing boundary from right side
    right_limit = (t.window_width() / 2) - 100
    #reducing boundary from top
    top_limit = (t.window_height() / 2) - 100
    #reducing boundary from bottom
    bottom_limit = (-t.window_height() / 2) + 100
    (x,y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

#Function for random movement of turtle
def move_turtle():
     if inside_window():
             angle = ri.randint(0,180)
             forw = ri.randint(0,200)
             t.right(angle)
             t.forward(forw)
     else:
             t.backward(200)

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed(1)
t.pensize(3)


while True:
    move_turtle()