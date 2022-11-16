while True:
    print('Você está no primeiro laço.')
    op_1 = input('Deseja sair? Digite SIM para isso. \n')
    if op_1 == 'SIM':
        break # Break referente ao primeiro laço
    else:
        while True:
            print('Você está no segundo laço')
            op_2 = input('Deseja sair do segundo laço? Digite SIM para isso. \n')
            if op_2 == 'SIM':
                break
    print('Você saiu do segundo laço')
print('Você saiu do primeiro laço')