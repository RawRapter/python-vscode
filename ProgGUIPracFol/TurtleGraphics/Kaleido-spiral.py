"""
Creating Kaleido Spiral.

Itertool.cycle : It iterates through each element in the input argument
and yields it and repeats the cycle and produces an infinite sequence of the argument

"""
import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','orange','yellow','blue','green','purple'])

#Function to create circle using specific radius ,angle and shift
def draw_circle(radius,angle,shift):
    t.pencolor(next(colors))
    t.circle(radius)
    t.right(angle)
    t.forward(shift)
    draw_circle(radius + 5,angle+1,shift+1)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)

draw_circle(30,0,1)

ti.sleep(3)
t.hideturtle()