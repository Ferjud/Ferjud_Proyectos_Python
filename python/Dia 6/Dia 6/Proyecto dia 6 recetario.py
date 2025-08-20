import os
from pathlib import Path
import shutil



def mostrar_recetas(carpetarec,nombrerut):
    rut = Path(nombrerut+"\\"+carpetarec)

    cont_recet = 0
    for recetas in Path(rut).glob("**/*.txt"):
        print(recetas.stem)

    print(f"tienes {cont_recet} guardadas en {carpetarec}")

def busq_dir_receta(valor_a_buscar,carpetarec,nombrerut):
    rut = Path(nombrerut + "\\" + carpetarec)
    recetavalidada=0
    for recetas in Path(rut).glob("**/*.txt"):
        if valor_a_buscar==recetas.stem:
            recetavalidada = recetas.name
    direccion=nombrerut+"\\"+carpetarec+"\\"+recetavalidada
    return direccion


def mostrarcategorias(categorias):
    for categ in categorias:
        print(categ)

def buscarcategorias(valor_a_buscar,categorias):
    catval=0
    for categ in categorias:
        if valor_a_buscar==categ:
            catval=categ

    return catval


def abrir_leer(archivo):
    abrir = open(archivo)
    print(abrir.read())




print("RECETARIO\n")

os.chdir("C:\\Users\\g\\Desktop\\Recetas")

nombre_ruta="C:\\Users\\g\\Desktop\\Recetas"

print("las recetas están ubicadas en la direccion de carpetas: "+ nombre_ruta)

carpeta=Path(nombre_ruta)

cont_receta=0
for recetas in Path(carpeta).glob("**/*.txt"):
    cont_receta+=1

print(f"tienes {cont_receta} recetas guardadas")


print("\n[1]-leer receta")
print("[2]-crear receta")
print("[3]-crear categoría")
print("[4]-eliminar receta")
print("[5]-eliminar categoría")
print("[6]-finalizar programa\n\n")


op = int(input("ingrese una opción: "))

while not(op>=1 and op<=6):
    op= int(input("ERROR.ingrese un numero entre 1 y 6"))

lista_cat=["Carnes","Pastas","Postres","Ensaladas"]

while op!=6:
    if op==1:
        mostrarcategorias(lista_cat)
        cat = input("escribe la categoría de la receta: ")
        mostrar_recetas(cat,nombre_ruta)
        reclect = input("elige la receta a leer: ")
        reclect = busq_dir_receta(reclect,cat,nombre_ruta)
        if reclect!=0:
            abrir_leer(reclect)
        else:
            print("nombre equivocado")

    elif op==2:
        mostrarcategorias(lista_cat)
        cat = input("elegir la categoría de la receta a ingresar: ")
        if cat!=0:
            nueva_receta = input("Escribe el nombre de la receta: ")
            abrir_receta = open(nombre_ruta+"\\"+cat+"\\"+nueva_receta+".txt","w")
            abrir_receta.write(input("Escribe la receta: "))
        else:
            print("Categoria equivocada")

    elif op==3:
        mostrarcategorias(lista_cat)
        cat = input("Escribe un nombre distinto para la categoría a crear:" )
        os.makedirs(nombre_ruta+"\\"+cat)
        lista_cat.append(cat)
        print("categoria creada")

    elif op==4:
        mostrarcategorias(lista_cat)
        cat = input("escribe la categoría de la receta: ")
        mostrar_recetas(cat, nombre_ruta)
        reclect = input("elige la receta a eliminar: ")
        reclect = busq_dir_receta(reclect, cat, nombre_ruta)
        if reclect != 0:
            os.remove(reclect)
            print("receta eliminada")
        else:
            print("nombre equivocado")

    elif op==5:
        mostrarcategorias(lista_cat)
        cat = input("elige la categoria a borrar: ")
        catborrar = buscarcategorias(cat,lista_cat)
        if catborrar != 0:
            shutil.rmtree(nombre_ruta+"\\"+catborrar)
            lista_cat.remove(catborrar)
            print("Se ha borrado la categoria")
        else:
            print("nombre equivocado")

    os.system("cls")

    cont_receta = 0
    for recetas in Path(carpeta).glob("**/*.txt"):
        cont_receta += 1

    print(f"tienes {cont_receta} recetas guardadas")

    print("\n[1]-leer receta")
    print("[2]-crear receta")
    print("[3]-crear categoría")
    print("[4]-eliminar receta")
    print("[5]-eliminar categoría")
    print("[6]-finalizar programa\n\n")

    op = int(input("ingrese una opción: "))



































