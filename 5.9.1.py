def do_n(f,n,s):
    '''Toma uma função f, um inteiro n e um argumento s para função f e chama a função n-vezes'''
    if n <= 0:
        return
    f(s)
    do_n(f,n-1,s)

do_n(print, 1000, "te amo")