import math

def mysqrt(a, x):
    while True:
        y = (x + a/x)/2
        if abs(x - y) < 0.0000000001:
            return y
            break
        x = y
        
def calc(a):
    print(float(a), ' ', round(mysqrt(a, 1), 11), ' ', round(math.sqrt(a), 11), ' ', abs(mysqrt(a,1) - math.sqrt(a)))    
        
def test_square_root(n):
    i = 1
    print('a', '   ', 'mysqrt(a)', '     ', 'math.sqrt(a)', '  ','diff')
    print('-', '   ', '---------', '     ', '------------', '  ','----')
    while i < n + 1:
        calc(i)
        i = i + 1
            
test_square_root(9)