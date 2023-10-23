num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[1] Converter para BINÁRIO\n[2] Converter para OCTAL\n[3] Converter para HEXADECIMAL')
base = int(input('Sua opção: '))
if base == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para Octal é igual a {oct(num)[2:]}')
else:
    print(f'{num} convertido para Hexadecimal é igual a {hex(num)[2:]}')
