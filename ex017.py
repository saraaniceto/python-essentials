import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(oposto**2 + adjacente**2)
print(f'A hipotenusa é: {hipotenusa:.2f}')