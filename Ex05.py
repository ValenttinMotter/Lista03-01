valor1 = int(input('Informe um valor: '))
valor2 = int(input('Informe outro valor: '))
valor3 = int(input('Informe um terceiro valor: '))

if valor1 > valor2 and valor1 > valor3:
    print(f'O menor valor é {valor3}')

    if valor3 % 2 == 0:
        print(f'O {valor3} é par')
    else:
        print(f'O {valor3} é ímpar')

elif valor2 > valor1 and valor2 > valor1:
    print(f'O menor valor é {valor1}')

    if valor1 % 2 == 0:
        print(f'O {valor1} é par')
    else:
        print(f'O {valor1} é ímpar')

else:
    print(f'O menor valor é {valor2}')

    if valor2 % 2 == 0:
        print(f'O {valor2} é par')
    else:
        print(f'O {valor2} é ímpar')