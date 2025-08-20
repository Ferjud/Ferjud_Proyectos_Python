def modificar_string(string):
    lista=list(string)
    nueva_lista=list(set(lista))
    nueva_lista.sort()
    return nueva_lista

print(modificar_string("jajaja"))


