nome = input('Digite seu nome completo: ').strip().title().split(" ")
print(f'Muito prazer em te conhecer!\nSeu primeiro nome é {nome[0]}\nSeu último nome é {nome[len(nome) - 1]}')