def is_power(a,b):
    if a == b:
        return True
    if a % b >= 1:
        return False

    return(is_power(a//b, b))    
print(is_power(1024, 2))