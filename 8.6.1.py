# -*- coding: utf-8 -*-
"""
Recebe uma palavra, uma letra e um número, retorna o índice da letra
se a palavra conter e começa a busca a partir do índice de número informado.
Se não houver a letra na palavra, retorna -1.

@author: neeg
"""

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1