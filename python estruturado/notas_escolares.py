def notas():
    count = 0
    for nota in range(0, 3):
        nota = eval(input('Informe sua nota: '))
        count = count + nota
        if nota > 10:
            print('Você deve informar uma nota menor que 10. Tente novamente.')
            exit()
    if nota >= 7:
        media = count / 3
        return f'Aprovado. Média = {media:.2f}'
    if nota >= 5:
        media = count / 3
        return f'Recuperação. Média = {media:.2f}'
    else:
        media = count / 3
        return f'Reprovado  Média = {media:.2f}'


print(notas())
