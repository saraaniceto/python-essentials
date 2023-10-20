dist = float(input('Qual é a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {dist}km')
preço = dist * 0.5 if dist <= 200 else dist * 0.45
print(f'A passagem irá custar: R${preço:.2f}')