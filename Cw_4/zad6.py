class Slowa:
    slowo1 = ""
    slowo2 = ""

    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2
    
    def wyswietl_wyrazy(self):
        print(self.slowo1 + ", " + self.slowo2)
    
    def sprawdz_czy_palindrom(self):
        if(self.slowo1 == self.slowo1[::-1] and self.slowo2 == self.slowo2[::-1]):
            return "Wyrazy są palindromami"
        elif(self.slowo1 == self.slowo1[::-1]):
            return "Slowo: " + str(self.slowo1) + " jest palindromem"
        elif(self.slowo2 == self.slowo2[::-1]):
            return "Slowo: " + str(self.slowo2) + " jest palindromem"
        else:
            return "Zaden z wyrazow nie jest palindromem"

    def sprawdz_czy_metagramy(self):
        if(len(self.slowo1) != len(self.slowo2)):
            return "Wyrazy nie są metagramami"
        ileRoznych = 0
        for x in range(0, len(self.slowo1)):
            if(self.slowo1[x] != self.slowo2[x]):
                ileRoznych += 1
            if(ileRoznych>1):
                return "Wyrazy nie są metagramami"
        return "Wyrazy są metagramami"

    def sprawdz_czy_anagramy(self):
        slowo1_list = list(self.slowo1)
        slowo2_list = list(self.slowo2)
        if len(self.slowo1) != len(self.slowo2):
            return "Wyrazy nie są anagramami"
        slowo1_list.sort()
        slowo2_list.sort()
        if(slowo1_list == slowo2_list):
            return "Wyrazy są anagramami"
        else:
            return "Wyrazy nie są anagramami"

s=Slowa("kajak", "data")
s.wyswietl_wyrazy()
print(s.sprawdz_czy_palindrom())
print(s.sprawdz_czy_metagramy())
print(s.sprawdz_czy_anagramy())