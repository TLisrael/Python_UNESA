unidade = 10
c_desconto10 = 0.1
c_desconto20 = 0.2

compras = eval(input('Informe quantas unidades deseja comprar: '))

calculo_base = unidade * compras

if compras <= 10:
    situacao = f'Não há descontos. O valor total foi de R${calculo_base:.2f}'
elif compras <= 20:
    valor_total = calculo_base * (1-c_desconto10)
    situacao = f'Foi concedido 10% de desconto. O valor total foi de R${valor_total:.2f}'
elif compras > 20:
    calculo_base = unidade * compras
    valor_total = calculo_base * (1 - c_desconto20)
    situacao = f'Foi concedido 20% de desconto. O valor total foi de R${valor_total:.2f}'

print(situacao)
