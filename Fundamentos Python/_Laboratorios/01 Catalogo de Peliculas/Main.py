from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

op = ""
while op != "4":
    print("1. Agregar Peliculas")
    print("2. Listar Peliculas")
    print("3. Eliminar archivo de Peliculas")
    print("4. Salir")
    op = input()
    
    if(op == "1"):
        nombre = input("Ingrese nombre: ")
        pelicula = Pelicula(nombre)
        print(pelicula)
        CatalogoPeliculas.agregarPelicula(pelicula)
    if(op == "2"):
        CatalogoPeliculas.listarPeliculas()
    if(op == "3"):
        CatalogoPeliculas.eliminarPeliculas()