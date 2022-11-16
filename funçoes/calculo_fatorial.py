# Estrategia 1

def fatorial_iterativo(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

# Estrategia 2
def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n-1)

numero = eval(input('Informe um número para saber o seu fatorial: \n'))
print(f'O fatorial iterativo {numero} é {fatorial_iterativo(numero)}')
print(f'O fatorial recursivo {numero} é {fatorial_recursivo(numero)}')