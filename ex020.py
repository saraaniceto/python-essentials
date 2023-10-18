import random

alunos = []
alunos.append(input('Digite o nome do 1º aluno: '))
alunos.append(input('Digite o nome do 2º aluno: '))
alunos.append(input('Digite o nome do 3º aluno: '))
alunos.append(input('Digite o nome do 4º aluno: '))
random.shuffle(alunos)
new_alunos = ", ".join(str(i) for i in alunos)


print(f'A ordem de apresentação será: {new_alunos}')