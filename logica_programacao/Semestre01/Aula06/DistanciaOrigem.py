import math
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

coordenadas = (x,y)

d = math.sqrt((x**2)+(y**2))

print(f"A distância das coordenadas {coordenadas} até a origem é, aproximadamente, {d:.2f}")
