# -*- coding: utf-8 -*-
"""
recebe uma string e um inteiro e devolve a string rotacionada por esse inteiro

@author: neeg
"""

def rotate_sord(word, n):
    new_word = ''
    for i in range(len(word)):
        ordem = ord(word[i]) + n
        new_word = new_word + chr(ordem)
    return new_word

print(rotate_sord('ibm', -1))