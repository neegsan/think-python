def ack(m,n):
    if not isinstance(n, int):
        print('The Ackermann funtion is defined for integers')
        return None
    
    elif not isinstance(m, int):
        print('The Ackermann funtion is defined for integers')
        return None
    
    elif m < 0 or n < 0:
        print('The Ackermann funtion is defined for integers non negative numbers')
        return None

    elif m == 0:
        return n + 1
        
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

print(ack(13,14))
