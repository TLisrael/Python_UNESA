from time import sleep


# Faça um programa que tenha uma função chamada contador()
# , que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

def contador(inicio, fim, passo):
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}')

    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(i)
    print('FIM! =]')


contador(0, 10, 1)
contador(10, 0, -2)
print('Personalize sua contagem! ')
i = int(input('Informe o inicio: '))
f = int(input('Informe o final: '))
p = int(input('Informe o passo a passo: '))

contador(i, f, p)
