from random import randint
def lanzar_dados():
 dado1 = randint(1,6)
 dado2=  randint(1,6)
 return dado1,dado2

def evaluar_jugada(d1, d2):
    suma_dados = d1 + d2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados>=10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"








lista_numeros = [1,2,15,7,2,8]

def reducir_lista(lista_numeross):
    lista_modificada = list(set(lista_numeross))
    maximo = max(lista_modificada)
    lista_modificada.remove(maximo)
    return lista_modificada

def promedio(lista_modificada):
    acu = 0
    cont = 0
    for n in lista_modificada:
        acu = acu + n
        cont = cont + 1
    return acu / cont







from random import choice


def lanzar_moneda():
    moneda = choice(["Cara", "Cruz"])
    return moneda

lista_numeros = [1, 2, 3, 4, 5]

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        lista = []
        print(moneda)
        print("la lista se autodestruira")
        return lista
    else:
        print(moneda)
        print("La lista fue salvada")
        return lista




























