def do_twice(f,x):
    f(x)
    f(x)

def print_twice(Line):
    print(Line)
    print(Line)

do_twice(print_twice,"spam")