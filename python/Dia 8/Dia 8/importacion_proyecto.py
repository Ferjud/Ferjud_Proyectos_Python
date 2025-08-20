def generar_P():
    n=1
    while True:
        yield f"P-{n}"
        n = n+1



def generar_F():
    n=1
    while True:
        yield f"F-{n}"
        n = n+1



def generar_C():
    n=1
    while True:
        yield f"C-{n}"
        n = n + 1





def decorar_turno(funcion):

    def otra_funcion(turno):
        print("su turno es:\n")
        funcion(turno)
        print("\nAguarde un momento y será atendido")
    return otra_funcion







