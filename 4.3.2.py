import turtle
    
def square(t,length):

    for i in range(4):
        t.fd(length)
        t.lt(90)

square(turtle.Turtle(),250)