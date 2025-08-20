print("Analizador de texto\n")
texto=input("Ingrese un texto: ")

texto= texto.lower()

print("Ingrese 3 letras a elección para analizar en el texto\n")
letra1=input("Ingrese letra 1:")
letra1=letra1.lower()

letra2=input("Ingrese letra 2:")
letra2=letra2.lower()

letra3=input("Ingrese letra 3:")
letra3=letra3.lower()


print(f"letra 1 aparece {texto.count(letra1)} veces en el texto")
print(f"letra 2: {texto.count(letra2)} veces")
print(f"letra 3: {texto.count(letra3)} veces")

texto_lista = texto.split()
print(texto_lista)
print(f"cantidad de palabras que hay en el texto: {len(texto_lista)}")


print(f"primera letra del texto: {texto[0]}")
print(f"ultima letra del texto: {texto[-1]}")

texto_lista.reverse()
texto_invertido=" ".join(texto_lista)
print(f"texto en orden inverso:  {texto_invertido}")

palabra_python = "python" in texto

dic={False:"no",True:"si"}

print(f"¿aparece la palabra python?: {dic[palabra_python]}")

























