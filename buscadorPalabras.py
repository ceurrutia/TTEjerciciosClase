def buscarPalabra():
        palabraBuscar = input("Ingresa tu palabra a buscar: ").lower()
        encontrado = False
        
        if palabraBuscar in listaPalabas:
            encontrado = True
            print(f"La palabra {palabraBuscar} esta en la lista") 
        else:
            print("No se ha encontado")
            
            
listaPalabas = []

while True:
    try: 
        print("1. Agrega palabras a la lista")
        print("2. Mostrar palabras ingresadas")
        print("3. Busca una palabra: ")
        print("4. Salir")
        opcion = int(input("Ingresa una opcion: "))
        
        if opcion == 1:
            palabraUser = input("Agrega una palabra: ").lower()
            listaPalabas.append(palabraUser)
            
        elif opcion == 2:
            print("**********Lista palabras **********")
            if len(listaPalabas) == 0:
                print("La lista esta vacia")
            else:
                for pal in listaPalabas:
                    print(pal) 
            
        elif opcion == 3:
            buscarPalabra()
            
        elif opcion == 4:
            print("Has salido del sistema. Adios")
            exit()
        
        else:
            print("Opcion no valida")
    except ValueError:
        print("Debes escribir un numero entero")
    

    
        
