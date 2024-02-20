def do_twice(f,x):
    f(x)
    f(x)

def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)

do_four(print,"amor")
