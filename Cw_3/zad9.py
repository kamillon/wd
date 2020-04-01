def ciag(*liczby ):
    if len(liczby) == 0:
        return 0
    else:
        suma=1
        for i in liczby:
            suma*=i
        return suma

print(ciag())
print(ciag(1,2,3,4))