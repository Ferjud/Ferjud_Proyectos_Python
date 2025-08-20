from random import choice


def pedir_letra():
    ing = input("letra: ")
    return ing


def validar(letra_ing):
    while not letra_ing.isalpha() or len(letra_ing) != 1:
        letra_ing = input("Error. Ingrese una letra válida: ")
    return letra_ing.lower()


def chequear_letra(letraval, palabra, pal_oculta, contvidas):
    lista_palabra = list(palabra)
    pal_oculta = list(pal_oculta)

    if letraval in lista_palabra:
        for pos in range(len(lista_palabra)):
            if lista_palabra[pos] == letraval:
                pal_oculta[pos] = letraval
        pal_oculta = "".join(pal_oculta)
        print("¡Acertaste! Palabra actual: " + pal_oculta)
    else:
        contvidas -= 1
        print("No acertaste. Te quedan " + str(contvidas) + " intentos.")

    return pal_oculta, contvidas


def resultado(palab_oculta, palabracorrecta, salirr):
    if palab_oculta == palabracorrecta:
        print("Felicidades, has ganado. La palabra era: " + palabracorrecta)
        salirr = 1
    return salirr


print("EL AHORCADO")

contadorvidas = 6
salir = 0
palabras = ["policia", "pizza", "automovil", "guitarra"]
adivinar = choice(palabras)
lista_adivinar = list(adivinar)
palabra_oculta = "-" * len(adivinar)

print("Ingresa letras para adivinar la palabra a continuación. Tienes 6 intentos a partir de ahora: " + palabra_oculta)

while contadorvidas > 0 and salir == 0:
    letra = pedir_letra()
    letra_validada = validar(letra)
    palabra_en_proceso, contadorvidas = chequear_letra(letra_validada, adivinar, palabra_oculta, contadorvidas)
    palabra_oculta = palabra_en_proceso
    salir = resultado(palabra_oculta, adivinar, salir)

if salir == 0:
    print("Has perdido. La palabra era: " + adivinar)



