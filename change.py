def change():
    expense = 23.75
    money = 100
    print(f'Ingresar gasto:\n' + f'{expense}')
    print(f'Dinero recibido\n' + f'{money}\n')
    print('Vuelto\n')
    print(f'Pesos:\n' + f'{int(money - expense)}')
    print(f'Centavos:\n' + f'{int(money / 4)}')
