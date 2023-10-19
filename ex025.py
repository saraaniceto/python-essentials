nome = input('Digite seu nome completo: ').strip().title()
print(f'Seu nome tem Silva? {nome.find("Silva") >= 0}')