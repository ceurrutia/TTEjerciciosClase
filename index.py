##recursivo

def factorizar(n):
    if (n == 0 or n == 1):
        return 1
    else:
        resultado = n * factorizar (n - 1)
        return resultado
    
print(factorizar(5))  


##iterativo

def fact(num):
    if (num == 0 or num == 1):
        return 1
    else:
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado

print(fact(5))

ciudades = ["madrid", "paris", "roma"]
print(ciudades[-1])

ciudades.append("brasilia")


for ciudad in ciudades:
    print(ciudad)
    
ciudades.pop()
    
print(ciudades)


## EJERCICIOS CLASE 3


lista= [2,3,4,5,90,45,60]
lista.sort()

print(lista[0]) 
print(lista.insert(2, 39))
print(lista)
print(lista.count(2))

for num in lista: 
    print(num)
    

print(lista)

print(1 == 2)


for i in range(1, 21):
    print(i)


print("****Tablas de multiplicar******")

num = int(input("Ingresa un numero para saber su tabla: "))

for i in range(1,11):
    resultado = num * i
    print(f' {num} * {i} es {resultado}')
    

####### GUARDAR DATOS EN UN TXT #####

import json

mydict = {
    1: {
        "titulo": "Catnip",
        "autor": "Rocchia",
        "year": 2024
    },
    2: {
        "titulo": "Cerro Torre",
        "autor": "Cesare Maestri",
        "year": 1969
    },
    3: {
        "titulo": "Grito de Piedra",
        "autor": "Werner Herzog",
        "year": 1986
    },
    
}

with open('mydict.txt', 'w') as miBase:
    json.dump(mydict, miBase)
    
print("Base de datos guardad en txt")

##Levantar desde txt

with open('mydict.txt', 'r') as miBase:
    nueva_carga = json.load(miBase)
    
    
print("lectura de base: ", nueva_carga)