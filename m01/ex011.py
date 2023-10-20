largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = round(largura * altura)
litros = round(area / 2)
print(f"""Sua parede tem a dimensão de {largura}m x {altura}m e sua área é de {area}m².
Para pintar essa parede, você precisará de {litros}l de tinta""")