nombre_curso = "Python"
nombre_lenguaje = nombre_curso

print(nombre_curso)
print(nombre_lenguaje)

numeros = [1,2,3]
numeros_copia = numeros

numeros_copia.append(20)

print(numeros)
print(numeros_copia)

##ALCANCE

##Global

##se define en cualquier lado

##Scope

def mostrarPares(numeros):
    numPares = list(filter(lambda num: num % 2 == 0, numeros))
    return numPares


pares = mostrarPares(numeros)
print(pares)

numbers = []
nombres = "Python"

def demo():
    ###Si quero definir una global dentro de una funcion para que o m cree otra
    global nombres
    nombres = "Java"
    print(numbers)
    print(nombres)
    numbers.append(22)
    
demo()
print(nombres)
print(numbers)

##fizzbuzz

def fizzBuzz():
    for i in range(1,31):
        
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
            
        elif i % 5 == 0:
            print("BUzz")
        else:
            print(i)
            
print(fizzBuzz())