produkty = {
    "ziemniaki" : "kg",
    "chleb" : "szt",
    "mąka" : "kg",
    "brokul" : "szt"
}

print(produkty)
lista = {key : value for key, value in produkty.items() if value == "szt"}
print(lista)