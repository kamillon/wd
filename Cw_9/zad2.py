import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

grupa = df.groupby(["Plec"]).agg({"Liczba":["sum"]})
wykres = grupa.plot.bar()
wykres.set_xlabel("Plec")
wykres.set_ylabel("Mln")
wykres.legend()
plt.title("Liczba urodzonych chłopcow i dziewczynek")
plt.show()