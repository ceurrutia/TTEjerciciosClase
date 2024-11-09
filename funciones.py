a = int(input("Ingrese un valor numerico: "))
b = int(input("Ingrese otro valor numerico: "))

def sumar(a,b):
    return a + b

print(f"El resultado de la suma es: {sumar(a,b)}")

def restar(a,b):
    return a - b

print(f"El resultado de la resta es: {(restar(a,b))}" )

def multiplicar(a,b):
    return a * b

print(f"El resultado de la multiplicacion es: {multiplicar(a,b)}")

def dividir(a,b):
    if (b == 0):
        return "No dividas por 0"
    else:
       return a / b
        
print(f"El resultado de la division es: {dividir(a,b)}") 

##encuentra una ciudad en una lista
##Aplica que sea insensible a mayuscula y minuscula

ciudadUsuario = input("Ingresa una ciudad: ")

listaCiudades = ["paris", "madrid", "Roma", "Bruselles"]
listaCiudades = [ciudad.lower() for ciudad in listaCiudades]

if (ciudadUsuario in listaCiudades):
    
    print("Esta en la lista")
else:
    print("No esta en la lista ")
    
##factorizar numero

def factorizar(num):
    if (num ==0 or num == 1):
        return 1
    else:
        res = num * factorizar (num -1)
        return res
        
print(factorizar(5))

##escriba una funcion que ingrese un numero entero y maneje el error

def ingresaEntero():
    try:
        while True:
            num = int(input("Ingrese un numero entero: "))
            if num < 0:
                print("El numero es negativo. Ingresa otro entero: (Para salir escribe 9)")
                print(f"El numero ingresado es {num} ")
                
            elif num == 9:
                print("Has salido del programa")
                return
    except:
        print("No se permiten caracteres. Solo puedes ingresar enteros")

ingresaEntero()  

##escribe una funcion que busque una palabra en un texto

texto = input("Escribe un texto: ")

def buscarPalabra():
    palabraUser = input("Introuduce una palabra a buscar: ")
    palabraBuscar = texto.split()
    encontrado = False
    
    if palabraUser in palabraBuscar:
        encontrado: True
        return "Se ha encontrado la palabra"
    else:
        return f'No se ha encontrado la palabra {palabraUser}'
        
print(buscarPalabra())         
    