##defino diccionario

mismascotas = {}

##funciones

def listarMascotas():
    if mismascotas:
        for nombre, datos in mismascotas.items():
            print(f"""
                  Mascota: {nombre} , especie: {datos['especie']}, edad: {datos['edad']}
                  """)
    else:
        print("*******No hay mascotas en la lista*********")
                
def agregarMascota():
    if opcion == 2:
        nombre = input("Ingresa el nombre de tu animalito: ")
        especie = input("Ingresa la especie de tu animalito: ")
        edad = int(input("Ingresa la edad de tu animalito: "))
        
    mismascotas[nombre] = {
    "especie": especie,
    "edad" : edad
    }
            
    print(f"Mascota {nombre} agregada correctamente.")   
    
def modificaMascota():
    nombre = input("Ingresa el nombre de la mascota a modificar: ")
    
    if nombre in mismascotas:
        especie = input("Ingrese nueva especie: ")
        edad = int(input("Ingrese nueva edad: "))
        mismascotas[nombre] = {
        "especie": especie,
        "edad" : edad
        }
        print(f" Modificacdos correctamente los datos de la mascota {nombre}")
        
    else:
        print("Animalito no encontrado")
        
def eliminarMascota():
    nombre = input("Ingresa el nombre de la mascota a eliminar: ")
    
    if nombre in mismascotas:
        del mismascotas[nombre]
        print("Animalito eliminado de la lista")
    else:
        print("NO se encontro animalito con ese nombre")
         

##Menu

while True:
    
    print("1. Lista mascotas")
    print("2. Agrega una nueva mascota")
    print("3. Modifica datos de una mascota")
    print("4. Elimina mascota")
    print("5. Salir del sistema")
    
    try:
        opcion = int(input("Ingresa tu opcion: "))
        
        if opcion == 1:
           listarMascotas() 
        elif opcion == 2:
            agregarMascota()
        elif opcion == 3:
            modificaMascota()
        elif opcion == 4:
            eliminarMascota()
        elif opcion == 5:
            print("Has salido del programa. Adios!")
            break
            
                
    except(ValueError):
        print("Opcion invalida")
    