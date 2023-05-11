lado_a = int(input('Digite um lado do triângulo: '))
lado_b = int(input('Digite o segundo lado do triângulo: '))
lado_c = int(input('DIgite um terceiro lado do triângulo: '))

if (lado_a + lado_b > lado_c) and \
    (lado_a + lado_c > lado_b) and \
    (lado_b + lado_c > lado_a):

    print('As medidas inseridas formam um triângulo: ')

    if lado_a == lado_b and lado_b == lado_c:
        print('Triângulo equilátero!')
    elif lado_a != lado_b and lado_b != lado_c:
        print('Triângulo escaleno!')
    else:
        print('Triângulo isósceles!')

else:
    print('As medidas inseridas não formam um triângulo')
