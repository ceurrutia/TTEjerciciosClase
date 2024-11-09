'''
Realizar una aplicación en Python que
A partir de la cantidad de litros de combustible que
consume un coche por cada 100 km de recorrido,
el costo de cada litro de combustible y la longitud
del viaje realizado (en kilómetros), muestra un
detalle de los litros consumidos y el dinero
gastado.
'''

# cantLitros = float
# costoPorLitro = float
# distanciaViaje = float

# ##devolver

# listrosUsados = float
# dineroGastado = float

#Programa

consumoCombustible100 = float(input("Ingrese el consumo de combustible  cada 100 km: "))
costoPorLitro = float(input("Ingrese el precio por litro: "))
distanciaViaje = float(input("Ingrese la distancia a recorrer: "))

## 1lt --> 100 km
## distancia = x

listrosUsados =  (distanciaViaje * consumoCombustible100) /100
print(f"los litros usados seran: {listrosUsados}")

dineroGastado = listrosUsados  * costoPorLitro
print(f"Dinero gastado:  { dineroGastado}")

##Len

texto = "hola"
nuevo_texto = len(texto)
print(nuevo_texto)

##Calcular el iva de u producto siendo que este es del 21%

producto = float(input("Ingrese un precio: "))
iva = 21

prodConIva = producto + (producto * iva /100)
print(f"El valor de tu producto sin iva es {producto}, con iva del 21% es {prodConIva}")
    
##Como funcion

def calcularIva(producto):
    if producto < 1200:
        print("No tienes recargos")
        return producto     
    else:
        productoIva = producto + (producto * iva / 100)
        print(f"El precio total con iva es {productoIva}")
        return productoIva

calcularIva(producto)