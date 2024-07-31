# Actividad 2- Primeros auxilios
# Contexto:

# En cualquier momento puede haber una emergencia y hay que estar preparados ¿sabrías
# cómo reaccionar en caso de que alguien necesite de primeros auxilios?
# Es muy probable que mucha gente no conozca cuáles son los pasos a seguir en caso de emergencia. 

# Por lo tanto, es importante conocer los primeros auxilios básicos para poder ayudar
# Este script interactivo tiene como objetivo guiar a través de los pasos críticos para 
# proporcionar primeros auxilios efectivos.



# Código:
while True:
    respuesta_estimulos = input("¿Responde a estímulos? (si/no): ").strip().lower()
    
    if respuesta_estimulos == 'si':
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
        break
    
    print("Abrir la vía aérea.")
    
    respira = input("¿Respira? (si/no): ").strip().lower()
    
    if respira == 'si':
        print("Permitirle posicisión de suficiente ventilación.")
        break
    
    print("Administrar 5 ventilaciones y llamar a la ambulancia.")
    
    while True:
        signos_vida = input("¿Signos de vida? (si/no): ").strip().lower()
        
        if signos_vida == 'si':
            print("Reevaluar a la espera de la ambulancia.")
        else:
            print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
        
        llego_ambulancia = input("¿Llegó la ambulancia? (si/no): ").strip().lower()
        if llego_ambulancia == 'si':
            print("Por finnnnn !!!! JEsuuuu , Maríaaaaa y Joséeee !.")
            break

    if llego_ambulancia == 'si':
        break
