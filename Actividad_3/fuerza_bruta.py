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

def fuerza_bruta(password):
    intentos = 0
    adivinado = ""
    
    for char in password:
        for letter in ascii_lowercase:
            intentos += 1
            if char == letter:
                adivinado += letter
                break
    
    return intentos

# Pide ontraseña 
password = getpass.getpass("Ingresa tu contraseña: ").lower()

# Calcula los intentos necesarios 
intentos = fuerza_bruta(password)

# Resultado nro intentos
print(f"La contraseña fue forzada en {intentos} intentos.")

