from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    modalidade = 'MIRIM'
elif idade <= 14:
    modalidade = 'INFANTIL'
elif idade <= 19:
    modalidade = 'JUNIOR'
elif idade <= 25:
    modalidade = 'SÊNIOR'
else:
    modalidade = 'MASTER'
print(f'O atleta é da modalidade {modalidade}')
