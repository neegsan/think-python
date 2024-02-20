def is_triangle(x, y, z):
    if x + y < z or y + z < x or z + x < y:
        print("Não é possível formar um triângulo!")
    else:
        print("É possível fornar um triângulo!")
