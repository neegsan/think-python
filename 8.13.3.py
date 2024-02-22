# -*- coding: utf-8 -*-
"""
nova versão simplificada da função que recebe uma palavra e
retorna se essa é um palíndrome ou não

@author: neeg
"""

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('reviver'))
print(is_palindrome('ovo'))
print(is_palindrome('marrocos'))
print(is_palindrome('bolalob'))
print(is_palindrome('sistema'))
print(is_palindrome('vermelhohlemrev'))