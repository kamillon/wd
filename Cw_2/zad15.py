while 1:
    try:
        x = float(input("Wprowadź liczbę: "))
        break
    except ValueError:
        print("Nieprawidłowe dane wejściowe ")