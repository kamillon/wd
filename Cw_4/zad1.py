import random as r
plik = open("Cw_4/liczby.txt", "w+")
for x in range(100):
    if x % 4 == 0:
        plik.write(str(x) + " ")
plik.close()