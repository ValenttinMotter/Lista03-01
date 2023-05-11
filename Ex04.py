valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
valor3 = int(input('Digite um terceiro valor: '))

if valor1 > valor2 and valor2 > valor3:
    print(f'O maior valor é {valor1}')

elif valor2 > valor1 and valor2 > valor3:
    print(f'O maior valor é {valor2}')

else:
    print(f'O maior valor é {valor3}')