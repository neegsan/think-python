import turtle
    
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def bob_arg():
    bob=turtle.Turtle()
    square(bob)

bob_arg()
