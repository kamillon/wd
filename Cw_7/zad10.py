import numpy as np

b = np.arange(81).reshape(9,9)
print(b)
print(b.shape,"\n")
c = b.reshape((27,3))
print(c)
print(c.shape,"\n")
d = c.reshape((3,27))
print(d)
print(d.shape,"\n")
e = d.ravel()
print(e)
print(e.shape,"\n")

# możemy utworzyć macierz o wymiarze kolumn i wierszy, których iloczyn jest równy liczbie elementów (81)
# liczbę kolumn i wierszy wybieramy z dzielników liczby elementów (81)
# macierz możemy spłaszczyć