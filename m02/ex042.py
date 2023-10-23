print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if (l1 >= l2 + l3) or (l2 >= l1 + l3) or (l3 >= l1 + l2):
    print ('Os segmentos acima não formam um triângulo')
else:
    print('Os segmentos acima formam um triângulo', end=' ') 
    if l1 == l2 and l1 == l3:
        print ('EQUILÁTERO')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('ESCALENO')
    else:
        print('ISÓCELES')
        