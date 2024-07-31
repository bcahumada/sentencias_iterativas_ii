while True:
    respuesta_estimulos = input("¿Responde a estímulos? (si/no): ").strip().lower()
    
    if respuesta_estimulos == 'si':
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
        break
    
    print("Abrir la vía aérea.")
    
    respira = input("¿Respira? (si/no): ").strip().lower()
    
    if respira == 'si':
        print("Permitirle posición de suficiente ventilación.")
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
