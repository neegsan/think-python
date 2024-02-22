# -*- coding: utf-8 -*-
"""


@author: neeg


def count(word, leter):
    count = 0
    for letter in word?:
        if letter == leter:
            count = count + 1
    return count
"""



def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count_2(word, letter, index):
    count = 0
    if find(word, letter, index) != -1:
        count = count + 1
        
    return count