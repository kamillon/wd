zdanie = input("Napisz zdanie: ")
print(zdanie.count(" "))


zad2
a = int(input("Podaj liczbę 1: "))
b = int(input("Podaj liczbę 2: "))
print(a * b)

zad4
liczba = int(input("Podaj liczbę: "))
print(abs(liczba))

zad5
a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
c = int(input("Podaj liczbę: "))
if 0 < a < 11 and (a>b or b>c):
  print("Warunki są spełnione")
else:
  print("Warunki nie są spełnione")


zad6
for x in range(0, 30, 5):
 print(x)

zad6 II
for x in range(0, 30, 5):
  if(x % 5 == 0):
    print(x)

zad7
for x in range(3):
  liczba = int(input("Podaj liczbę: "))
  print(liczba, pow(liczba,2))
