# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# e ‘N’, se seu argumento for zero ou negativo.

def positivo_negativo(n=0):
    if n >= 1:
        msg = 'Numero positivo'
    else:
        msg = 'Numero negativo'
    return msg


print(positivo_negativo())
