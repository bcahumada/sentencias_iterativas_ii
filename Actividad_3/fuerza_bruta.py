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

