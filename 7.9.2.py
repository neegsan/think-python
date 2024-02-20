while True:
    nome = input('Digite numeros para avaliarmos:')
    if nome == 'done':
        break       
    print(eval(nome))
print('Done!')