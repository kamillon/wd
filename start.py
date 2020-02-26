print ("Hello world!")

# for element in kolekcja:
#   for element2 in kolekcja2:

def funkcja():
  print("Ala")
  a = 5
  imie = "Zbyszek"

a = 5
print(type(a))

imie = "Ala"
imie = 'Ala'
imie = """Ala
ma kota
Filemona"""

print(type(imie))
imie = 6
print(type(imie))
imie = 6.3
print(type(imie))

# def funkcje():
#   """dosctring"""
#   pass



# liczba = int(5)
# liczba = int("5")
# liczba = int("5.5")

imie = "ala"
imie = imie.capitalize()
print(imie)
print(imie[0])
# imie[0] = "a"   blad
print("ala".capitalize().count("A"))

print(imie + imie)
# print(5 + imie)
#formatowanie wyjscia
print("Ala ma 5 lat")
# print(imie + "ma" + 5 + "lat")  blad
print(imie + "ma" + str(5) + "lat") 
print("{} ma {} lat".format(imie, 5))
print("{0} ma {1} lat".format(imie, 5))
wiek = 5
print(f"{imie} ma {wiek} lat")

#listy

lista = []
lista = [1, 4, "Ala", 4.5, imie, [1,2]]
lista[0]
lista[5][1]
lista.append(3)
lista[0] = 10
lista2 = lista + lista
lista_nowa = list()

#slownik

slownik = {}
slownik = {"imie": "Marek", 
"wiek": 35}
slownik["imie"]
slownik.keys()
print(slownik.values())
print(slownik.items())

def pow():
  pass

from math import *
import math as m
from math import pow

pow()
m.pow()