# Actividad 3- Fuerza bruta
# Contexto:

# ¿Qué tan seguro es tu password?
# Este código es para determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en
# minúscula. El programa intenta todas las combinaciones de letras  posibles, en orden alfabético, hasta 
# que la combinación de letras sea igual a la de la contraseña indicada. 
# Este proceso se realiza letra por letra, de izquierda a derecha.



# Código:
from string import ascii_lowercase
import getpass

# Pide contraseña
password = getpass.getpass("Ingresa tu contraseña: ").lower()

# Contador de intentos y la cadena 
intentos = 0
adivinado = ""

# Realiza el proceso de fuerza bruta
for char in password:
    for letter in ascii_lowercase:
        intentos += 1
        if char == letter:
            adivinado += letter
            print(f"Letras adivinadas hasta el momento: {adivinado}")
            break

# Resultado del número de intentos
print(f"La contraseña fue forzada en {intentos} intentos.")
