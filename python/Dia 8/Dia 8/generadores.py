def generar():
    n = 1
    while True:
        yield n
        n = n + 1


generador = generar()
print(next(generador))
print(next(generador))




def generar():
    n = 7
    while True:
        if n % 7 == 0:
            yield n
        n += 1


generador = generar()
print(next(generador))






def generar():
    vidas = 3
    while vidas >= 0:
        yield vidas
        vidas = vidas - 1


perder_vida = generar()

while True:
    vida_actual = next(perder_vida)

    if vida_actual >= 2:
        print(f"Te quedan {vida_actual} vidas")
    elif vida_actual < 2 and vida_actual > 0:
        print(f"Te queda {vida_actual} vida")
    elif vida_actual==0:
        print("Game Over")
        break


def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()






