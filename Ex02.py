valor = int(input('Digite um valor: '))

if valor >= 0:
    raiz = valor ** (1/2)
    print(f'A raiz quadrada do valor dado é {raiz:.2f}')

else:
    potencia = valor ** 2
    print(f'O quadrado do valor dado é {potencia:.2f}')