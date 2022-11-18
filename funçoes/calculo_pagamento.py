def horas_trabalhadas(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if qtd_horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))
    return salario


str_horas = eval(input('Informe as horas '))
str_taxa = eval(input('Informe a taxa '))
total_salario = horas_trabalhadas(str_horas, str_taxa)
print(f'O valor dos seus rendimentos é de R$ {total_salario}')
