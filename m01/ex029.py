vel = float(input('Qual é a velocidade atual do carro? '))
if (vel > 80):
    print('MULTADO! Você excedeu o limite de velocidade de 80km/h')    
    multa = (vel - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança')
