def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')


contador(4, 4, 7, 6, 2)
contador(2, 4, 6, 9, 0)
contador(2, 4, 3)
contador(8, 0)


# ----------xx-----------------xx-------------------------xx------------------

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
