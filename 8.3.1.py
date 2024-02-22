"""
recebe um string e imprime suas letras na ordem contrária

@author: neeg
"""
def invertion(s):
    index = len(s)-1
    while index > -1:
        letter = s[index]
        index = index - 1
        print(letter)
        
invertion('guardanapo')