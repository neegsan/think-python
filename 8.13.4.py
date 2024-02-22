# -*- coding: utf-8 -*-
"""
Esta função recebe uma string como argumento e verifica se a primeira
letra é minúscula retornando um booleano verdadeiro ou falso

@author: neeg
"""

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True                     #interrompe a função
            
        else:
            return False                    #interrompe a função


#-----------------------------------------------------------------

"""
Esta função recebe uma string como argumento e retorna a string 'True'
independentemente do seu argumento, pois a terceira linha do código
verifica se a string 'c' é minúscula e devolve 'True' se sim.

@author: neeg
"""

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            print('True')
            return 'True'
        else:
            print('False')
            return 'False'
        
        
#-----------------------------------------------------------------

"""
Esta função recebe uma string como argumento e retorna o booleano True
se a última letra for minúscula. Ela percorre cada letra da string e grava
Trur na variável flag se a letra for minúscula ou senão grava False, após
isso ela imprime a variável.

@author: neeg
"""

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


#-----------------------------------------------------------------

"""
Esta função recebe uma string como argumento e retorna um valor booleano.
A variável flag é booleana e no loop for ela altera seu valor para True se
houver uma letra minúscula na palavra e não haverá outra alteração no valor

@author: neeg
"""

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower() #se flag=True, sempre será True
        print(flag)
    return flag


#-----------------------------------------------------------------

"""
Esta função recebe uma string como argumento e retorna um valor booleano.
Ela verifica se a primeira letra do argumento é maiúscula e retorna o booleano
False no caso afirmativos e encerra o código. Se a primeira letra for minúscula
ela pula o condicional if e retorna True. Ou seja, a função verifica se a
primeira letra do código é minúscula.

@author: neeg
"""

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True