
from servicios.conexion_bd import *

from funciones import VerListado, agregarAnime, listarCategorias, modificarAnime, buscarAnime, eliminarAnime, listarSorted, generarReporteBajoStock, verStockActual
   
##Menu

while True:

     try:
          print("-------------------------------")
          print(" ***** Menu de opciones ***** ")
          print("-------------------------------")
          print("1. Agregar nuevo anime ")
          print("2. Listar animes")
          print("3. Listar categorias")
          print("4. Buscar anime")
          print("5. Eliminar anime ")
          print("6. Modificar registro")
          print("7. Listar animes ordenados alfabeticamente")
          print("8. Consulta animes con stock menor a 3 unidades")
          print("9. Ver stock actual de productos ")
          print("10. Salir")
          print("-------------------------------")
          

          opcion = int(input("Ingrese opcion: "))

          if opcion == 1:
               agregarAnime()
          elif opcion == 2:
               VerListado()
          elif opcion == 3:
               listarCategorias()
          elif opcion == 4:
               buscarAnime()
          elif opcion == 5:
               eliminarAnime()
          elif opcion == 6:
               modificarAnime()
          elif opcion == 7:
               listarSorted()
          elif opcion == 8:
               generarReporteBajoStock()
          elif opcion == 9:
               verStockActual()
          elif opcion == 10:
               print("Has salido del sistema. Adios.")
               conexion.close()
               exit()
          else:
               print("Opcion no valida")

     except (ValueError):
          print("Debe ingresar solo numeros enteros")
          

