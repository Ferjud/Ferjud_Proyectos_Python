def devolver_distintos(n1,n2,n3):
    lista=[n1,n2,n3]
    if (n1+n2+n3)>15:
        return max(lista)
    elif (n1+n2+n3)<10:
        return min(lista)
    elif (n1+n2+n3)>=10 and (n1+n2+n3)<=15:
        if (n1>n2 and n1<n3) or (n1>n3 and n1<n2):
            return n1
        elif (n2>n1 and n2<n3) or (n2>n3 and n3<n1):
            return n2
        else:
            return n3


print(devolver_distintos(5,4,2))






