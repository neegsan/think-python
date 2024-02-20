def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def line_plus():
    print("+",4*"- "+"+",4*"- "+"+")

def line_bar():
    print("|         |         |")

def grade():
    line_plus()
    do_four(line_bar)
    line_plus()
    do_four(line_bar)
    line_plus()

grade()