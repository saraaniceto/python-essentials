from math import sin, cos, tan, radians

angle = float(input('Digite um ângulo: '))
angle_radians = radians(angle)

print(f'O ângulo {angle} tem o SENO de {sin(angle_radians):.2f}')
print(f'O ângulo {angle} tem o COSENO de {cos(angle_radians):.2f}')
print(f'O ângulo {angle} tem a TANGENTE de {tan(angle_radians):.2f}')