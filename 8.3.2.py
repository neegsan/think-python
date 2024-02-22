# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:07:28 2024
imprimindo nome dos patinhos em ordem alfabética

@author: neeg
"""

prefixes = 'JKLMNOPQ'
sufixes = 'ack'
for letter in prefixes:
    if letter == 'Q' or letter == 'O':
        print(letter + 'u' + sufixes)
    else:
        print(letter + sufixes)