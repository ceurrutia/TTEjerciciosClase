productos = {"Manzanas": 50, "Peras": 30, "Bananas": 40}
productos["Naranjas"] = 25


print(productos)

midiccionario = {"frutas": 5, "verduras": 10, "carnes": 4}
midiccionario["aves"] =8

print(midiccionario)

for clave, valor in midiccionario.items():
    print(f"{clave}: {valor}")


ciudades = {"mardid": 50000, "paris": 40000}

ciudades["locateli"]= 80000
print(ciudades)

for clave, valor in ciudades.items():
    print(f"{clave}: {valor}")
    
for clave, valor in sorted(ciudades.items(), key=lambda x: x[1]):
    print(f"{clave}: {valor}")
    
    
canciones = {
   
    "titulo": input("Ingrese titulo: "),
    "autor": input("Ingrese autor: "),
    "anio": int(input("Ingrese anio: ")),
    "banda": input("Ingrese nombre de la banda: ")
    
}

print(canciones)