print("adivina el numero\n")

nombre=input("Ingresa tu nombre:")

from random import *

N= randint(1,101)

print("He pensado un numero del 1 al 100 y si lo adivinas, ganas. Tienes 8 intentos")

intentos=8

while intentos>0:
    num = int(input(f"por favor {nombre} ingresa un numero:"))
    intentos=intentos-1
    if num==N:
        print(f"Felicidades, has acertado el numero {N} y te han sobrado {intentos} intentos")
        break
    elif num > N:
        print(f"el numero escrito es mayor al numero obejtivo, tienes {intentos} intentos")
    elif num < N:
        print(f"el numero escrito es menor al numero objetivo, tienes {intentos} intentos")
    else:
         print(f"el numero ingresado esta fuera del rango (1,100), tienes {intentos} intentos")

if intentos==0:
    print(f"perdiste, te has quedado sin intentos y el numero era {N}")





