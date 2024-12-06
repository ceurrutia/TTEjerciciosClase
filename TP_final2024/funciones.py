
from servicios.conexion_bd import *

##Diccionario

listaAnime = {}

## METODOS FUNCIONES TODAS

##GET 
def VerListado():
    cursor.execute('SELECT * FROM anime')
    animes = cursor.fetchall()
    print("***** Lista de animes en venta en la coleccion ***** \n")
    
    if not animes:
        print("No hay registros ingresados")
    else:
        listaAnime.clear()  
        for anime in animes:
           
            listaAnime[anime[0]] = {
                "titulo": anime[1],
                "resumen": anime[2],
                "director": anime[3],
                "categoria": anime[4],
                "año": anime[5],
                "episodios": anime[6],
                "rating": anime[7],
                "precio": anime[8],
                "stock": anime[9]
            }
        
        
        for id_anime, detalles in listaAnime.items():
            print(f"ID: {id_anime}")
            for key, value in detalles.items():
                print(f"{key.capitalize()}: {value}")
            print("\n")

##CREATE
def agregarAnime():
    
    titulo = input("Ingrese titulo: ")
    resumen = input("Ingrese resumen: ")
    director = input("Ingrese director: ")
    categoria = input("Ingrese categoria: ")
    año = int(input("Ingrese año de estreno: "))
    episodios = int(input("Ingrese cantidad de episodios: "))
    rating = float(input("Ingrese rating: "))
    precio = float(input("Ingrese precio: "))
    stock = int(input("Ingrese stock: "))

    cursor.execute("INSERT INTO anime (titulo, resumen, director, categoria, año, episodios, rating, precio, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (titulo, resumen, director, categoria, año, episodios, rating, precio, stock))
    conexion.commit()
    
    print("Nuevo anime agregado exitosamente")


##CATEGORIAS GET

def listarCategorias():
     cursor.execute('SELECT categoria, COUNT(*) FROM anime GROUP BY categoria')
     categorias = cursor.fetchall()
     
     if categorias:
         
          print("****** Categorias y cantidad de animes en ellas **** \n")
          for categoria, cantidad in categorias:
               print(f"Categoria: {categoria} \nCantidad: {cantidad}") 
     else:
          print("No se encontraron categorias ")
                 
     
          
##Modifica registros, UPDATE, set       

def modificarAnime():
    animeABuscar = input("Ingrese el nombre del anime a modificar: ").lower()
    
    cursor.execute("SELECT * FROM anime WHERE LOWER(titulo) = ?", (animeABuscar,))
    anime = cursor.fetchone()
    
    if anime:
        print(f"Se ha encontrado anime con nombre {anime[1]}")
        nuevo_nombre = input("Modifique nombre: ")
        nuevo_resumen = input("Modifique resumen: ")
        nuevo_director = input("Modifique nombre del director: ")
        nueva_categoria = input("Modifique categoria: ")
        nuevo_año = input("Modifique el año de estreno: ")
        nuevo_episodios = input("Modifique la cantidad de episodios: ")
        nuevo_rating = input("Modifique el rating: ")
        nuevo_precio = float(input("Ingrese nuevo precio: "))
        nuevo_stock = int(input("Ingrese nuevo stock: "))
        
        cursor.execute("""
            UPDATE anime SET titulo = ?, resumen = ?, director = ?, categoria = ?, año = ?, episodios = ?, rating = ?, precio = ?, stock = ?
            WHERE id = ?
        """, (nuevo_nombre, nuevo_resumen, nuevo_director, nueva_categoria, nuevo_año, nuevo_episodios, nuevo_rating, nuevo_precio, nuevo_stock, anime[0]))
        
        conexion.commit()
        print("Anime modificado exitosamente")
        
    else:
        print("No se ha encontrado anime con ese nombre")

##GET

def buscarAnime():  
     
     animeBuscar = input("Ingrese el titulo del anime que desea buscar: ").lower() 
     cursor.execute("SELECT * FROM anime WHERE LOWER(titulo) = ?", (animeBuscar,))
     anime = cursor.fetchone()
     
     if anime:
          print(f"Se ha encontrado el anime {anime[1]}, Resumen: {anime[2]}, Director: {anime[3]} ")
     else:
          print("No hay anime con ese titulo en la lista")
     


##DELETE
def eliminarAnime():
     try:
          animeEliminar = int(input("Introduce el ID del anime que quieres eliminar: "))
          cursor.execute("SELECT id FROM anime WHERE id = ?", (animeEliminar)) 
          anime = cursor.fetchone()
          
          if anime:
               cursor.execute("DELETE id FROM anime WHERE id = ?", (animeEliminar))
               conexion.commit()
               print(f"El anime {animeEliminar} ha sido eliminado del listado.")
          else:
               print("No se ha encontrado anime con ese ID")
     except ValueError:
          print("El ID siempre es un numero entero")
          
          
##GET ORDENADO ALFABETICAMENTE
         
def listarSorted():
           cursor.execute('SELECT * FROM anime ORDER BY titulo ')
           animes = cursor.fetchall()
           print("***** Lista de animes ordenados ***** \n")
          
           for anime in animes:
               print(f"ID: {anime[0]}, Titulo: {anime[1]}, Resumen: {anime[2]}, Director: {anime[3]}, Categoria:  {anime[4]}, Año: {anime[5]}, Episodios: {anime[6]}, Rating: {anime[7]}, Precio: {anime[8]}\, Stock: {anime[9]}n")

##GET DE UN ATRIBUTO MENOR A UN MUMERO
          
def generarReporteBajoStock():
     cursor.execute('SELECT * FROM anime WHERE stock <=3 ORDER BY titulo ')
     animes = cursor.fetchall()
     
     print("***** Lista de animes con stock menor a 3 unidades ***** \n")
     print("**** ALERTA BAJO STOCK **** \n ")
     if animes: 
         
          for anime in animes:   
               print(print(f"ID: {anime[0]}, Titulo: {anime[1]}, Resumen: {anime[2]}, Director: {anime[3]}, Categoria:  {anime[4]}, Año: {anime[5]}, Episodios: {anime[6]}, Rating: {anime[7]}, Precio: {anime[8]}\, Stock: {anime[9]}\n"))
     else:
          print("No se han encontrado animes con bajo stock")

##Ver stock

def verStockActual():
          cursor.execute('SELECT titulo, stock FROM anime')
          stock = cursor.fetchall()
          
          if stock:
            
              print("***** STOCK ACTUAL DE PRODUCTOS ******* \n")
             
              for anime in stock:
                    print(f"Titulo: {anime[0]}, Stock: {anime[1]}\n")
          else:
               print("No se han encontrado animes sin stock")

