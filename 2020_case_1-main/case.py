import turtle as tl
import math


def triangle(x, y, z, color):
    tl.up()
    tl.goto(x, y)
    tl.down()
    tl.color(color)
    tl.begin_fill()
    tl.left(45)
    tl.fd(z * math.sqrt(2) / 2)
    tl.left(135)
    tl.fd(z)
    tl.left(135)
    tl.fd(z * math.sqrt(2) / 2)
    tl.end_fill()
    
tl.done()
