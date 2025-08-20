def ceros_seguidos(*args):
    cont=0
    for arg in args:
        if arg==0:
            cont+=1
        else:
            cont=0

        if cont==2:
           return True
        else:
           return False

print(ceros_seguidos(1,2,0,5,0))