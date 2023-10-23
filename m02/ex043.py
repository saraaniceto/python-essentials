peso = float(input('Qual é o seu peso(kg)? '))
altura = float(input('Qual é a sua altura(m)? '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso ideal')
elif imc < 30:
    print('Você está em sobrepeso')
elif imc < 40:
    print('Você está em obesidade')
else:
    print('Você tem obesidade mórbida')
    