class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


mago = Mago()
arquero = Arquero()
samurai = Samurai()

personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()






class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(objeto):
    objeto.defender()





