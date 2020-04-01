wysokosc = int(input("Podaj wysokosc: "))
if(wysokosc <= 10):
    for i in range(wysokosc+1):
        print(i * "A")
else:
    print("Za duza wysokosc")