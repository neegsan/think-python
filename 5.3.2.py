def is_triangle(x, y, z):
    if x + y < z or y + z < x or z + x < y:
        print("Não é possível formar um triângulo!")
    else:
        print("É possível fornar um triângulo!")

def triangle(x,y,z):
    x = input("Insira o lado x do triângulo.")
    y = input("Insira o outro lado y do triângulo.")
    z = input("Insira o último lado z do triângulo.")
    int(x,y,z)
    is_triangle(x,y,z)