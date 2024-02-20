import math

def hypotenuse(c_a,c_o):
    hypotenuse_squared = c_a**2 + c_o**2
    hypotenuse = math.sqrt(hypotenuse_squared)

    return hypotenuse

print(hypotenuse(3.19,4.25))
