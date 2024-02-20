def gcd(a,b):
    if a == 0:
        return b
    
    elif b == 0:
        return a
    
    if a > b:
        r = a % b
    if a < b:
        r = b % a
        a = b    
        
    elif r == 0:
        return b
                
    return gcd(b,r)
        


print(gcd(23732, 180))
print(gcd(360, 120))