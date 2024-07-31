#import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Solicita umbral
try:
    umbral = int(input("Introduce el umbral de ventas: "))
except ValueError:
    print("Por favor, introduce un número entero válido para el umbral.")
    exit(1)

# Diccionario vacío
ventas_filtradas = {}

# Loop para filtrar las ventas 
for mes, valor in ventas.items():
    if valor > umbral:
        ventas_filtradas[mes] = valor

# Ventas por sonbre el umbral
print(ventas_filtradas)
