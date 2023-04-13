largura = float(input('Digite a largura da casa: '))
comprimento = float(input('Digite o comprimento da casa: '))

area = largura * comprimento

energiaNecessaria = area * 18

print(f'Quantidade correta de Watts para iluminação adequada é de {energiaNecessaria:.2f} watts')