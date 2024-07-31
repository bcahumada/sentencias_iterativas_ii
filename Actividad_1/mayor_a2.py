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
    umbral = int(input("Cuál es el umbral de ventas?: "))
except ValueError:
    print("Error: introduce un número entero válido para el umbral. Ejemplo: 70000")
    exit(1)

# Filtra las ventas > umbral
ventas_filtradas = {mes: valor for mes, valor in ventas.items() if valor > umbral}

# muestra mes y ventas
print(ventas_filtradas)
