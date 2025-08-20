#si todos los elementos de la lista son positivos devuelve true, sino false.
def todos_positivos(lista_numeros):
    for num in lista_numeros:
        if num < 0:
            return False
        else:
            pass

    return True







lista_numeros = [-2, 100, 500, 1500]

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma = suma + n

    return suma






lista_numeros = [1, 2, 4, 5, 6, 8, 9]

def cantidad_pares(lista_num):
    cont = 0
    for n in lista_num:
        if n % 2 == 0:
            cont = cont + 1

    return cont