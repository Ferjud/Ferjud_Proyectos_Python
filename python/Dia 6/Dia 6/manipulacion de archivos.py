archivo=open("pruebas.txt")
print(archivo.read())


file=open("texto.txt")
print(file.readline())



documento=open("texto.txt")
linea1=documento.readline()
linea2=documento.readline()
print(linea2)




archivo2=open("mi_archivo.txt","w")
archivo2.write("Nuevo texto")
archivo2.close()
archivo3=open("mi_archivo.txt")
print(archivo3.read())




archivo4=open("mi_archivo.txt","a")
archivo4.write("Nuevo inicio de sesión")
archivo4.close()
archivo5=open("mi_archivo.txt")
print(archivo5.read())



registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

regis=open("registro.txt","a")
for item in registro_ultima_sesion:
    regis.writelines(item + "\t")
regis.close()

registro=open("registro.txt")
print(registro.read())





