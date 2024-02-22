# -*- coding: utf-8 -*-
"""
Correção do progarma que recebe duas palavras e compara se uma é o inverso
da outra
word1 -> 'pots'		word2 -> 'stop'
i = 0 -> p		    j = 3 -> p
i = 1 -> o		    j = 2 -> o
i = 2 -> t		    j = 1 -> t
i = 3 -> s		    j = 0 -> s

@author: junio
"""
def reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j > -1:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True
            