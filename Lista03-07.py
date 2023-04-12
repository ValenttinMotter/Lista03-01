duplicata = float(input('Digite o valor da duplicata: '))

diasAtraso = int(input('Digite a quantidade de dias atrasados: '))

multaPorDia = 0.05 * diasAtraso
totalMulta = multaPorDia * diasAtraso

total = duplicata + totalMulta

print(f'O total a pagar é R$ {total:.2f}')