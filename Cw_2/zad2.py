import sys

print("Podaj liczbe")
x = sys.stdin.readline()
x = int(x)
y = sys.stdin.readline()
y = int(y)
wynik = x * y
wynik = str(wynik)
sys.stdout.write(wynik)