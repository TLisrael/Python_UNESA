# Faça um programa que tenha uma função chamada área()
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento):
    a = largura * comprimento
    return a


largura_teste = eval(input('Informe a largura do terreno: '))
comprimento_teste = eval(input('Informe o comprimento do terreno: '))

resultado = area(largura_teste, comprimento_teste)
print(f'área total do terreno: {resultado}m²')
