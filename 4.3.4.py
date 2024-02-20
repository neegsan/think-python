import turtle
    
def polygon(t,length,n):
    
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    n=150
    length=(r*2*3.141592653589793)/n
    polygon(t,length,n)

circle(turtle.Turtle(),20)