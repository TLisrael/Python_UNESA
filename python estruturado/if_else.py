def maior_numero():
    numero1 = eval(input('Informe o primeiro número: '))
    numero2 = eval(input('Informe o segundo número: '))

    if numero1 > numero2:
        return numero1
    else:
        return numero2
print(maior_numero())

# xxxxxxxxxxxxxxxx ---- xxxxxxxxxxxxx ---- xxxxxxxxxxxxxx -----
numero1 = eval(input('Informe o primeiro número: '))
numero2 = eval(input('Informe o segundo número: '))
maior_numero = numero2
if numero1 > numero2:
    maior_numero = numero1
print(f'O maior número é: {maior_numero}')


