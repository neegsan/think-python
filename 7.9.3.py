# -*- coding: utf-8 -*-
""" aproxima math.pi a partir da série de Ramanujan """
import math

''' função que recebe k e devolve o fatorial de 4k '''

def factorial_four(k):
    result = 1
    if k == 0:
        return 1
    
    else:
        k = 4*k
        while k > 0:
            fac = k*(k - 1)
            result = fac*result
            k = k - 2
        return result
    
""" função que receve k e devolve 26390 vezes K e soma com 1103 """

def multiples_sum(k):
    result = 1103 + 26390*k
    return result

""" recebe k e devolve o fatorial de k elevado a 4 """

def factorial_exp(k):
    result = 1
    if k == 0 or k == 1:
        return 1
    
    else:
        while k > 1:
            fac = k*(k - 1)
            result = fac*result
            k = k - 2
        return result**4
    
""" recebe k e devolve 396 elevado a 4 vezes k """

def exponential_four(k):
    result = 396**(4*k)
    return result

''' recebe k e devolve a fração da série de Ramanujan aplicada em k '''

def frac(k):    
    frac = (factorial_four(k)*multiples_sum(k))/(factorial_exp(k)*exponential_four(k))
    return frac
    
'''recebe k e devolve a k-ésima soma parcial de ramanujan '''

def partial(k):
    const = (2*math.sqrt(2))/9801
    result = const*frac(k)
    return result

def estimate_pi():
    sigma = 0
    k = 0
    while sigma < 1e-15:
        sigma = sigma + partial(k)
        k = k + 1
    return 1/sigma

print(estimate_pi())