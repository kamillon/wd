class Ciagi:
    ciag=[]
    a1 = 0
    r = 0
    n = 0
  
    def wyswietl_dane(self):
        print(self.ciag)
    
    def pobierz_elementy(self):
        print("Podaj wartosci ciagu")
        print("Wpisz 'stop' aby zakończyć")
        while True:
            wejscie = input()
            if wejscie == 'stop':
                break
            self.ciag.append(int(wejscie))

    def pobierz_parametry(self,a1,r,n):
        self.a1 = a1
        self.r = r
        self.n = n
    
    def policz_sume(self):
        suma = 0
        for x in range(self.n):
            suma += self.a1 + x * self.r
        print(suma)

    def policz_elementy(self):
        for x in range(self.n):
            print("a" + str(x+1) + " = " + str(self.a1 + x * self.r))

c = Ciagi()
c.pobierz_elementy()
c.wyswietl_dane()
c.pobierz_parametry(1,3,3)
c.policz_sume()
c.policz_elementy()