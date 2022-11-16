def encontrar_pares(lista):
    pares = lista[0]
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma = soma + numero
    return soma
lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = encontrar_pares(lista_teste)
print(f'A soma dos pares é [{par}]')


# Solução do professor
def ehPar(n):
    r = n % 2 == 0
    return r


def somar_par(lst):
    soma = 0
    for num in lst:
        if ehPar(num):
            soma += num
        return soma


lista = [10, 2, 5, 7, 6, 3]
soma = somar_par(lista)
print(f'O somatório dos elementos pares da lista é {soma}')