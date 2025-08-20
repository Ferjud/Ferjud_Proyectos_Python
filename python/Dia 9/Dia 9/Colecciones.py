from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador=Counter(lista)



from collections import defaultdict

mi_diccionario=defaultdict(lambda: "Valor no hallado")

mi_diccionario["edad"]=44

mi_diccionario["peso"]

print(mi_diccionario)




from collections import deque

lista=["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

lista_ciudades=deque(lista)

lista_ciudades.appendleft("Milan")

print(lista_ciudades)






