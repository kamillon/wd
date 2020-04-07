with open("Cw_4/liczby.txt", "w+") as plik:
    for x in range(5):
        tekst = input("Wpisz tekst: ")
        plik.write(tekst + "\n")


with open("Cw_4/liczby.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")