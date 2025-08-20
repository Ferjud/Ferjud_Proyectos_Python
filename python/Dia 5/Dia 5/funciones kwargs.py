def cantidad_atributos(**kwargs):
    cont = 0
    for arg in kwargs:
        cont += 1
    return cont






def lista_atributos(**kwargs):
    valores = kwargs.values()
    print(valores)
    lista = list(valores)
    return lista

print(lista_atributos(a="1",b="2"))






def describir_persona(nombre, **kwargs):
    print(f"características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

