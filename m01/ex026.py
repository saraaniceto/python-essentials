from unidecode import unidecode

frase = input('Digite uma frase: ').strip()
newFrase = unidecode(frase).lower()
print(f'A letra A aparece {newFrase.count("a")} vezes\nA primeira letra A apareceu na posição {newFrase.find("a") + 1}\nA última letra A apareceu na posição {newFrase.rfind("a") + 1}')j