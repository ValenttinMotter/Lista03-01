valorConta = float(input('Digite o valor da conta: '))
valorPago = float(input('Digite o valor pago: '))

troco = valorConta - valorPago

cedulasCentenas = int(troco / 100)
cedulasDezenas = int(troco / 10) - 10 * cedulasCentenas
cedulasUnidades = int(troco) - 100 * cedulasCentenas - 10 * cedulasDezenas 

print(f'O valor do troco é {troco} R$ e suas notas respectivas para fechar o valor são {cedulasCentenas:.0f} de 100 reais')
print(f'{cedulasDezenas:.0f} de 10 reais')
print(f'{cedulasUnidades:.0f} de 1 real')