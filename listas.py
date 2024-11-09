numeros = [23, 5, 8, 90, 12]
ordenados = sorted(numeros)
print(ordenados)
animales = ["gato", "perro", "canario"]
animales.append("loro")
print(animales)

mascotas = []


while True:
    print("Seleccione opcion: ")
    print("1. agrega animalito")
    print("2. salir")
    
    
    opcion = int(input("Ingresa tu opcion: "))
    
    if opcion == 1:
        mascotaUser = input("Ingresa tu mascota: ")
        mascotas.append(mascotaUser)
        print(f"Se ha agregado a {mascotaUser}")
    elif opcion == 2:
        print("Adios")
        break
    else:
        print("Opcion inavalida")
        
##Operador & en sets

s1 = {1,2,34,5}
s2 = {4,5,6,7}
print(s1&s2)