# Minha solução
def encontrar_minimo(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo


lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontrar_minimo(lista_teste)

print(f'O menor elemento da lista é: [{menor}]')



