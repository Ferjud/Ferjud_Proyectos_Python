def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2
    return suma

suma_cuadrados(1, 2, 3)


def suma_absolutos(*args):
    acu = 0
    for arg in args:
        if arg < 0:
            arg = arg - arg * 2
            acu += arg
        else:
            acu += arg
    return acu

suma_absolutos(2, 3, 5, -7)




def numeros_persona(nombre,*args):
    suma_numeros=sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


def cantidad_atributos(**kwargs):
    cont = 0
    for arg in kwargs:
        cont += 1
    return cont








