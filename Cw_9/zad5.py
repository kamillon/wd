import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('zamowienia.csv', header = 0, delimiter = ";")

grupa = df.groupby("Sprzedawca").agg({"idZamowienia":["count"]})

wykres = grupa.plot.bar()
wykres.set_ylabel("Liczba zamowien")
wykres.set_xlabel("Sprzedawca")
wykres.legend()
plt.title("Liczba zlozonych zamowien przez poszczegolnych sprzedawcow")
plt.show()