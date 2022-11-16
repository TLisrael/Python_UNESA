def eh_primo(n):
    if n < 2:
        return False  # Se o numero for menor que 2 o numero nao é primo
    i = n // 2  # Senão, pegamos a divisão inteira do numero
    while i > 1:  # E enquanto o numero for maior do que 1
        if n % i == 0:  # Teste se o numero % divisao inteira dele mesmo é igual a zero. Se for
            return False  # Retorne falso e mostre que não é um numero primo
        i = i - 1  # Se não, diminua e decremente até o numero 1 e retorne que é verdadeiro
    return True


def imprimir_resultado(numero, resultado):
    msg = f'O numero {numero} nao é primo'
    if resultado:  # Se o resultado for verdadeiro
        msg = f'O numero {numero} é primo'
    return msg


numero = eval(input('Informe um numero: \n'))
resultado = eh_primo(numero)
msg = imprimir_resultado(numero, resultado)
print(msg)
