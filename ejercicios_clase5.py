
##Mayor de 3 numeros
def esMayor(a,b,c):
    if a>b:
        print(f"El mayor es {a}")
    elif b > c:
            print(f"El mayor es {b}")
    elif c > a:
        print(f"El mayor es {c}")
    else:
        print("error")

print(esMayor(4,7,44))

palabras= []

def agregarPalabras():
    palabraUser = input("Ingrese una palabra: ").lower()
    palabras.append(palabraUser)
    print( f"palabra ingresada: {palabraUser}")
    

def buscarPalabra():
    encontrado = False
    palabraBuscar = input("Ingrese la palabra a buscar: ").lower()
    
    if palabraBuscar in palabras:
        encontrado = True
        
        return f"La palabra buscada: {palabraBuscar} esta en la lista"
    else:
        return f"La palabra {palabraBuscar} no esta siendo encontrada, o sea"

while True:
        try:
            print("1. Agrega una palabra") 
            print("2. Muestra todas las palabras ingresadas") 
            print("3. Busca una palabra") 
            print("4. Salir") 
            opcion = int(input("Selecciona una opcion: "))
            
            if (opcion == 1):
                agregarPalabras()
            elif (opcion ==2):
                if len(palabras)==0:
                    print("**** No hay registros ingresados ****")
                else: 
                    for palabra in palabras:
                        print(palabra)
            elif (opcion == 3):
                print(buscarPalabra())
                
            elif (opcion == 4):
                print("Has salido del programa. Adios")
                break 
            else:
                print("Opcion no valida. ")
        except:
            print("Solo se permiten numeros enteros")
   



      

    