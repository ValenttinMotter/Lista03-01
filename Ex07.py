nota = float(input('Insira a nota do aluno: '))

if nota < 0 or nota > 10:
    print('Nota Inválida')
elif nota >= 9:
    print('Classificação Superior')
elif nota >= 7:
    print('Classificação Médio Superior')
elif nota >= 5:
    print('Classificação Médio')
elif nota >= 3:
    print('Classificação Médio Inferior')
elif nota >= 0.1:
    print('Classificação Inferior')
else:
    print('Sem Rendimento')