def mysqrt(a, x):
    while True:
        y = (x + a/x)/2
        if abs(x - y) < 0.0000000001:
            print(y)
            break
        x = y
        
mysqrt(16, 1)