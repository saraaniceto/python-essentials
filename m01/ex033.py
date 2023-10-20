num1 = float(input('Digite o 1º valor: '))
num2 = float(input('Digite o 2º valor: '))
num3 = float(input('Digite o 3º valor: '))
valores = [num1, num2, num3]
valores.sort()
print(f'O menor valor digitado foi: {valores[0]}\nO maior valor digitado foi: {valores[2]}')