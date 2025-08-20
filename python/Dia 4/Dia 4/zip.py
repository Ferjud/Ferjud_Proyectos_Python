capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for capital,pais in zip(capitales,paises):
    print(f"La capital de {pais} es {capital}")


marcas = ["Adidas","Puma","Nike"]
productos =["botines","remeras","pantalones"]

mi_zip= zip(marcas,productos)
print(list(mi_zip))




lista1= ["uno","dos","tres","cuatro","cinco"]
lista2= ["um","dois","três","quatro","cinco"]
lista3= ["one","two","three","four","five"]

numeros= list(zip(lista1,lista2,lista3))
print(numeros)


