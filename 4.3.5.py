import turtle
    
def polygon(t,length,n,angle):
    
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

def circle(t,r,angle):
    n=150
    length=(r*2*3.141592653589793)/n
    polygon(t,length,n,angle)

circle(turtle.Turtle(),20,90)