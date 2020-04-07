class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
        
    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        print(str(self.x) + " " + str(self.y))
    
    def __del__(self):
        print("Robaczek zginął")

robak = Robaczek(0, 0, 1)
robak.idz_w_gore(1)
robak.pokaz_gdzie_jestes()
robak.idz_w_prawo(5)
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo(2)
robak.pokaz_gdzie_jestes()
robak.idz_w_dol(3)
robak.pokaz_gdzie_jestes()