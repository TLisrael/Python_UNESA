def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando valores {valores} temos {s}')


soma(5, 2)
soma(4, 5, 7)
