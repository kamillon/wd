class Material:

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    
    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania(Material):

    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(self.rozmiar, self.kolor, self.dla_kogo)

class Swetry(Ubrania):

    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        print(self.rodzaj_swetra)

m = Material("bawelna", 5, 4)
m.wyswietl_nazwe()
print(m.dlugosc)
u = Ubrania("M", "czarny", "mezczyzna")
u.wyswietl_dane()
s = Swetry("z golfem")
s.wyswietl_dane()
s.rodzaj = "jedwab"
s.wyswietl_nazwe()