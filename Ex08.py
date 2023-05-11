funcao = str(input('Digite a função desempenhada: '))
horas_trab = float(input('Insira o número de horas trabalhados: '))

if funcao == 'Testador':
    valor_hora = 20
elif funcao == 'Analista de Testes':
    valor_hora = 35
elif funcao == 'Programador':
    valor_hora = 45
elif funcao == 'Analista de Sistemas':
    valor_hora = 40
elif funcao == 'DBA':
    valor_hora = 50

else:
    print('Função não encontrada')

salario = float(valor_hora) * horas_trab

print(f'Sua função é {funcao} e seu salário é de R$ {salario} !')

