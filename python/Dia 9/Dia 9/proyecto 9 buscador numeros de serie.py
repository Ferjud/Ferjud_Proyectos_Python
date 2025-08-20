import os
import re
import datetime
import time
import math

inicio = time.time()
i = 0

fecha=datetime.date(2025,4,5)

hoy=fecha.today()
dia_hoy = hoy.day
mes_hoy = hoy.month
año_hoy = hoy.year

fecha_actual = f"{dia_hoy}/{mes_hoy}/{año_hoy}"


print(f"fecha de búsqueda: {fecha_actual}")

ruta = "C:\\Users\\g\\Desktop\\Python\\Dia 9\\Mi_Gran_Directorio"
patron = r"N\w\w\w-\d\d\d\d\d"

print("\tARCHIVO\t\t\t NRO.SERIE")
for carpetas, subcarpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        ruta_completa = carpetas+"\\"+archivo

        # Abrir el archivo
        arch = open(ruta_completa, "r")
        contenido = arch.read()  # Leer la única línea
        arch.close()  # Cerrar el archivo manualmente

        # Buscar el número de serie en el contenido
        nro_serie = re.search(patron, contenido)
        if nro_serie:
            print(f"{archivo}\t\t{nro_serie.group()}")
            i = i + 1

print(f"numeros encontrados: {i}")

final = time.time()

duracion = final-inicio

duracion_redondeada = math.ceil(duracion)
print(f"duración de ejecución: {duracion_redondeada}")













