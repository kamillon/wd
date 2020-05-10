import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

grupa = df.groupby(["Rok"]).agg({"Liczba":["sum"]})
wykres = grupa.plot(xticks=grupa.index.values)
wykres.set_xlabel("Rok")
wykres.set_ylabel("Liczba urodzonych")
plt.title("Liczba urodzonych w danym roku")
plt.legend()
plt.show()
