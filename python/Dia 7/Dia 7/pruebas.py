class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        # Llamar al constructor de Persona directamente
        Persona.__init__(self, nombre, apellido)  # Inicializa la clase base
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)  # Convertir balance a float

    @classmethod
    def imprimir(cls, instancia):
        print("\n")
        print(instancia.nombre)
        print(instancia.apellido)
        print(instancia.numero_cuenta)
        print(instancia.balance)

    @classmethod
    def depositar(cls, instancia):
        cantdep = float(input("Ingrese dinero a depositar: "))  # Convertir a float
        instancia.balance += cantdep

    @classmethod
    def retirar(cls, instancia):
        cantret = float(input("Ingrese dinero a retirar: "))  # Convertir a float

        if cantret <= instancia.balance:  # Usar <= para permitir retirar el saldo exacto
            instancia.balance -= cantret
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

  nuevo_cliente.imprimir(nuevo_cliente)

  op = int(input("1-retiro, 2-depósito,0-finaliza"))

  while op!=0:

      if(op==1):
          nuevo_cliente.retirar(nuevo_cliente)
      else:
          nuevo_cliente.depositar(nuevo_cliente)

      nuevo_cliente.imprimir(nuevo_cliente)

      op = input("1-retiro, 2-depósito,0-finaliza")














