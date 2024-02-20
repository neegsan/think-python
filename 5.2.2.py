def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def fermat(a, b, c, n):
    a = input("Digite a primeira parcela a")
    b = input("Digite a segunda parcela b")
    c = input("Digite o resultado da soma das duas parcelas c")
    n = input("Digite o expoente n de ambos os valores fornecidos")
    int(a, b, c, n)
    check_fermat(a, b, c, n)
