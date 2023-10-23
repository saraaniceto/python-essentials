valor = float(input('Valor da casa: R$'))
salary = float(input('Salário do do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcel = valor / (anos * 12)
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${parcel:.2f}')
if parcel > salary * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')

