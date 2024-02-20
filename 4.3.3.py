import turtle
    
def polygon(t,length,n):

    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(turtle.Turtle(),50,6)