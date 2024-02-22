# -*- coding: utf-8 -*-
"""
recebe uma palavra e retorna se essa é um palíndrome ou não

@author: neeg
"""

def is_palindrome(word):
    for i in range(len(word)):
        if word[i] == word[len(word)-(i+1)]:
            x = True

        else:
            x = False
    return x

print(is_palindrome('reviver'))
print(is_palindrome('ovo'))
print(is_palindrome('marrocos'))
print(is_palindrome('bolalob'))
print(is_palindrome('sistema'))
print(is_palindrome('vermelhohlemrev'))
