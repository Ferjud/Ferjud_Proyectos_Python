import re

def verificar_email(email):
    buscar = re.search(r"@", email)

    buscar2 = re.search(r"\.com$", email)

    if buscar and buscar2:
        print("Ok")

    else:
        print("La dirección de email es incorrecta")


import re


def verificar_saludo(frase):
    buscar = re.search(r"^Hola", frase)

    if buscar:
        print("Ok")
    else:
        print("No has saludado")




import re

def verificar_cp(cp):
    patron = r"\w\w\d\d\d\d"

    resultado = re.search(patron, cp)

    if resultado:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

