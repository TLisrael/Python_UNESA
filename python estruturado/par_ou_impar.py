def par_impar():
    numero = eval(input('Informe o numero para saber se é par ou ímpar: '))

    if numero % 2 == 0:
        return 'Número par'
    else:
        return 'Número impar'
print(par_impar())