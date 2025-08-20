def contar_primos(num):
    cont_pri=0
    for numero in range(2,num+1):
        divisores = 0
        for n in range(1,numero+1):
            if numero%n==0:
                divisores+=1

        if divisores == 2:
            cont_pri += 1

    return cont_pri

print(contar_primos(37))