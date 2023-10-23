nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno foi {media:.1f}')
if media < 5:
    print('Aluno REPROVADO')
elif media < 7:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno APROVADO')