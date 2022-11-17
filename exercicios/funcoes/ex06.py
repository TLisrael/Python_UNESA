# Faça um programa que tenha uma função chamada escreva()
# que receba um texto qualquer como parÂmetro e mostre uma mensagem
# com tamanho adaptavel

def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f' {texto} ')
    print('~' * tam)


# programa principal
escreva('Olá, mundo!')
escreva('Tudo de bom')
escreva('que bela onda ')