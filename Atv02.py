parcelasPagas = int(input('Quantas parcelas foram pagas?: '))

totalParcelas = 24
valorParcelas = 1000
totalPago = parcelasPagas * valorParcelas
saldoDevedor =(totalParcelas - parcelasPagas) * valorParcelas

print(f'O valor total pago é de {totalPago}, e o saldo devedor é de {saldoDevedor}')