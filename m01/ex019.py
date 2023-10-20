import random

alunos = []
alunos.append(input('Digite o nome do 1º aluno: '))
alunos.append(input('Digite o nome do 2º aluno: '))
alunos.append(input('Digite o nome do 3º aluno: '))

print(f'O aluno selecionado foi {random.choice(alunos)}')