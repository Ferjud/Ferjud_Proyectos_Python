def abrir_leer(arch):
    abrir = open(arch)
    return abrir.read()


def sobrescribir(arch):
    archivo = open(arch, "w")
    archivo.write("contenido eliminado")

def registro_error(arch):
    archivo = open(arch, "a")
    archivo.write("se ha registrado un error de ejecución")
     archivo.close()




