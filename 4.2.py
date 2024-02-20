import turtle

def polygon(t,length,n,angle):
    
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

def circle(t,r,angle):
    n=150
    length=(r*2*3.141592653589793)/n
    polygon(t,length,n,angle)

def petalas(t,r,angle):
    for i in range(2):
        circle(t, r, angle)
        t.lt(180-angle)

def flor(n,t,r,angle):
    for i in range(n):
        petalas(t,r,angle)
        t.lt(360/n)

flor(20,turtle.Turtle(),10,90)