import turtle
import math


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


def diag(t, length, n):
    polygon(t, length, n)
    t.lt(360/n)
    t.fd(length/(2*math.cos(360/n)))
    for i in range(2*n-2):
        t.rt(360-2*(360/n))
        t.fd(length/(2*math.cos(360/n)))
        t.lt(360)
        t.fd(length/(2*math.cos(360/n)))


diag(turtle.Turtle(), 100, 6)
