from pathlib import Path



ruta_base=Path.home()
print(ruta_base)

ruta_original=Path("Curso Python","Día 6","practicas_path.py")
ruta=ruta_original.relative_to("Curso Python")
print((ruta))



directorio=Path.home()
ruta2=Path(directorio,"Curso Python","Día 6","practicas_path.py")


nombre_sin_extension=ruta2.stem

print(nombre_sin_extension)

