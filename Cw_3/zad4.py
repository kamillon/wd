def monotonicznosc(a):
    if(a > 0):
        return "Funkcja rosnaca"
    elif(a == 0):
        return "Funkcja stala"
    else:
        return "Funkcja malejaca"

print(monotonicznosc(1))
print(monotonicznosc(0))
print(monotonicznosc(-1))