import math

def calcular_circunferencia(radio):
    pi = round(math.pi, 6)  # Valor de pi redondeado a 6 decimales
    circunferencia = 2 * pi * radio
    return circunferencia

# Radios dados
radios = [3, 8, 10]

# Calcular y mostrar circunferencia para cada radio
for radio in radios:
    circunferencia = calcular_circunferencia(radio)
    print(f"Para un radio de {radio}, la circunferencia es: {circunferencia}")
