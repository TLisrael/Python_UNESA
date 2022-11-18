from math import ceil


def calculo_imc(peso, altura):
    imc = peso / altura ** 2
    return imc


peso = eval(input('Informe o seu peso: '))
altura = eval(input('Informe sua altura: '))

imc = ceil(float(calculo_imc(peso, altura)))

print(f'Seu IMC é de {imc:.2f}')
