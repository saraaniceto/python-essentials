cidade = input('Digite o nome da cidade onde você nasceu: ').strip().title()
print(cidade.startswith("Santo ") or cidade.startswith("São ") or cidade.startswith("Santa "))