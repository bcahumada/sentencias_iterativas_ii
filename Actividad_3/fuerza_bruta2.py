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
