class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        Persona.__init__(self, nombre, apellido)  # Llamada directa al constructor de Persona
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)  # Convertir balance a float

    def imprimir(self):
        print("\nDatos del Cliente:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Nro de cuenta: {self.numero_cuenta}")
        print(f"Balance: {self.balance}")

    def depositar(self):

        cantdep = float(input("Ingrese dinero a depositar: "))  # Convertir a float
        while cantdep<0:
            print("Error\n")
            cantdep = float(input("Ingrese dinero a depositar: "))

        self.balance += cantdep

    def retirar(self):

        cantret = float(input("Ingrese dinero a retirar: "))  # Convertir a float
        while cantret < 0:
            print("Error\n")
            cantret = float(input("Ingrese dinero a retirar: "))

        if cantret <= self.balance:  # Usar <= para permitir retirar el saldo exacto
            self.balance -= cantret
        else:
            print("Error. Se intentó retirar más del dinero existente.")


def crear_cliente():
    nomb = input("Ingrese nombre: ")
    ap = input("Ingrese apellido: ")
    nrocuenta = input("Ingrese nro de cuenta: ")
    bal = input("Ingrese balance: ")

    return Cliente(nomb, ap, nrocuenta, bal)


def inicio():
    nuevo_cliente = crear_cliente()

    nuevo_cliente.imprimir()

    op = int(input("1-retiro, 2-depósito, 0-finaliza: "))

    while op!=1 and op!=2 and op!=0:
        print("Error. Ingrese numero valido\n")
        op = int(input("1-retiro, 2-depósito, 0-finaliza: "))


    while op != 0:
        if op == 1:
            nuevo_cliente.retirar()
        elif op == 2:
            nuevo_cliente.depositar()

        nuevo_cliente.imprimir()

        while op != 1 and op != 2 and op != 0:
            print("Error. Ingrese numero valido\n")
            op = int(input("1-retiro, 2-depósito, 0-finaliza: "))


# Llamada a la función principal
inicio()















