cadena = "1234"
enteros = 1234
mifloat = 23.5

##CONVERSIONES

print(int(cadena))
print(str(enteros)) 
print(float(cadena))

##COMPARACION

lista = [23, 24, 11, 7, 5, 45, 40]

def imprimerPares(lista):
    pares = []
    for num in lista:
        
        if num % 2 == 0:
            pares.append(num)
        print(pares )
        
        
print(imprimerPares(lista))


nombre, apellido = input("ingrese nombre: "), input("ingrese apellido: ")

print( "hola, " , nombre , apellido)

#Tipar que sea numero

minumero = int(input("Ingrese un numero: "))
minumero2 = int(input("Ingrese un numero: "))
print(minumero * minumero2)


##EJERCITACIONES DE CLASE

#PROMEDIO

notasUsuario = int(input("Ingrese cantidad de notas: "))

##Creo un array vacio para que se vaya llenado con las notas
notas = []

for i in range(notasUsuario):
    nota = float(input("Ingrese una nota: "))
    notas.append(nota)
    
##promediar

def promediar(notas):
    suma = sum(notas)
    prom = suma / len(notas)
    
    return prom

print("El promedio de las notas ingresadas es: ", promediar(notas))
    

##Realiza las siguientes operaciones: suma,
##resta, multiplicación, y módulo.

a = 20
b = 50

def suma(a,b):
    return a + b
print("la suma de los numeros es: ", suma(a, b) )

a = 200
b = 50

def resta(a,b):
    return a - b
print("la resta de los numeros es: ", resta(a, b) )

a = 20
b = 70

def multiplicacion(a,b):
    return a * b
print("la multiplicacion de los numeros es: ", multiplicacion(a, b) )

a = 20
b = 2

def division(a,b):
    if b == 0:
        return print("No se divide por 0")
    else:
        return a / b

print("la division de los numeros es: ", division(a, b) )

##Modulo

number = 3
if number % 2 == 0:
    print("Es par")
else:
    print("Es impar")
    
##Calculadora de propinas

montoTotal = float(input("Ingrese el monto total consumido: "))
propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))
 
def calcularPropina(montoTotal):
    aPagar = montoTotal * (propina /100)
    return aPagar

print(f"La propina adecuada para su mesa es {calcularPropina(montoTotal)} " )
print(f"El monto total a pagar es: ", montoTotal + calcularPropina(montoTotal))