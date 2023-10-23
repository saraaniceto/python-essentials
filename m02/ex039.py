from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
ano_alistamento = ano_nasc + 18
print(f'Quem nasceu em {ano_nasc} tem {idade} anos.')
if idade < 18 :
    print(f' Ainda falta(m) {18 - idade} ano(s) para o alistamento\n Seu alistamento será em {ano_alistamento}')
elif idade > 18 :
    print(f'Você já deveria ter se alistado há {idade - 18} anos.\nSeu alistamento foi em {ano_alistamento}')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')