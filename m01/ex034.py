sal = float(input('Qual o salário do funcionário? R$'))
if sal <= 1250:
    novo_sal = sal * 1.15
else:
    novo_sal = sal * 1.10
print (f'Quem ganhava R${sal:.2f} passa a ganhar R${novo_sal:.2f}')