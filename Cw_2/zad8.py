lista = []
print("Podaj liczby całkowite, które chcesz umieścić w pętli.")
print("Wpisz 'stop' aby zakończyć")
while True:
    wejscie = input()
    if wejscie == 'stop':
        break
    lista.append(int(wejscie))

print("Twoja lista -> " + repr(lista))