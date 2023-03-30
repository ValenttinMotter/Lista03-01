quantidade = int(input('Digite a quantidade do produto: '))

preçoUnit = float(input('Digite o valor unitário: '))

desconto = float(input('Digite o desconto a ser dado: '))

totalComDesconto = (quantidade * preçoUnit) * (1 - desconto/100)

print(f'O total com desconto será R$ {totalComDesconto} R$')


