print("Calculadora de comisiones")

nombre = input("Ingresa nombre del vendedor: ")

valorventas = input("Ingresa el valor de las ventas: ")

valorventasint = int(valorventas)

print(f"Al vendedor {nombre} le corresponde una comision de {round(((valorventasint*13)/100),2)}")



