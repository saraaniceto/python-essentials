from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
num = randint(0,5)
aposta = int(input('Em que número você pensou? '))
print('PROCESSANDO...')
sleep(2)
if aposta == num:
    print(f'VOCÊ GANHOU! O número que eu pensei foi {num}')
else:
    print(f'GANHEI! Eu pensei no número {num} e não no {aposta}')