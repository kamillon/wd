import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

p = df[((df["Rok"] <= 2017) & (df["Rok"] > 2012))]
grupa = p.groupby(["Plec"]).agg({"Liczba":["sum"]})

wykres = grupa.plot.pie(subplots=True, autopct="%.2f %%", figsize=(6,6))
plt.title("Ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach")
plt.show()