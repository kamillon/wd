class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_prodkukt(self):
        print(self.nazwa_produktu)
        print(str(self.ilosc))
        print(self.jednostka_miary)
        print(str(self.cena_jed) + "\n")
    
    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary + "\n")

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

produkt = NaZakupy("banany", 2, "kg", 4.99)
produkt.wyswietl_prodkukt()
produkt.ile_produktu()
print(produkt.ile_kosztuje())