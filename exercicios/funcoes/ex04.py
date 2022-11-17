# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(list):
    maior = list[0]
    for i in list:
        if i > maior:
            maior = i
    return maior


lista_teste = [5, 6, 4, 3, 7, 9, 15, 303]
maior_numero = maior(lista_teste)
print(maior_numero)
""