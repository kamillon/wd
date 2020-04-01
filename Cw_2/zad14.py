while 1:
    try: 
      a = int(input("Podaj liczbę do spierwiastkowania: "))
      assert a > 0 
      break
    except AssertionError :  
      print("liczba jest ujemna")

print(a**0.5)