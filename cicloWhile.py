##OPERADOR TERNARIO EN PYTHON

edad = int(input("Dime tu edad: "))
acceso = "Puedes pasar" if edad >= 18 else "No puedes"
print(f"Por tu edad: {edad}, {acceso}")


# numero = int(input("Ingresa un numero: "))
# suma = 0

# while True:
#     print("Sales marcando 1")
#     suma = numero + suma
#     print(f"La suma de los nuemros ahora es: {suma}" )
#     numero = int(input("Ingresa un numero: "))
#     if (numero == 1):
#         print("Has salido. Adios")
#         exit()
        
##EJEMPLO compra 3 productos
opcion_compra = -1 ## para ingresar al bucle

while opcion_compra != "4":

        print("**** Productos a comprar del menu: **** ")
        print('''
            1. pizza
            2. milanesa
            3. hamburgeusa
            4. salir
        ''')
        opcion_compra = input("Ingresa el numero que quiera de producto: ")

        if opcion_compra == "1":
            print("Compraste pizza")
        elif opcion_compra == "2":
            print("Compraste milanesa")
        elif opcion_compra == "3":
            print("Compraste hamburguesa")
        elif opcion_compra == "4":
            print("Adios")
            exit()
        else:
            print("Emmm, no. Elije una opcion valida")
            

