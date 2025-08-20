from importacion_proyecto import *

def imprimir_turno(turno):
    print(turno)

print("\n\n\t\tTURNOS\n\n")

# Inicializar los generadores fuera del bucle
generador_P = generar_P()
generador_F = generar_F()
generador_C = generar_C()

# Decorar la función de impresión una vez
imprimir_turno_decorado = decorar_turno(imprimir_turno)

while True:

    categoria = input("P-perfumes, F-farmacia, C-cosméticos: ").upper()

    if categoria == "P":
        turno = next(generador_P)
        imprimir_turno_decorado(turno)

    elif categoria == "F":
        turno = next(generador_F)
        imprimir_turno_decorado(turno)

    elif categoria == "C":
        turno = next(generador_C)
        imprimir_turno_decorado(turno)

    else:
        print("Categoría inválida. Por favor, ingrese P, F o C.")