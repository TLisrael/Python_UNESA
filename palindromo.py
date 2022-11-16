palindromo = input('Informe uma palavra: ')

if palindromo == palindromo[::-1]:
    print('Palindromo')
else:
    print('Não é palindromo')