import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
ch = df[df["Plec"]=='M'].groupby(['Rok']).sum()
dz = df[df["Plec"]=='K'].groupby(['Rok']).sum()

plt.bar(df.Rok.unique(),[ch.values[y][0] for y in range(len(ch.values))],color="green", label="M")
plt.bar(df.Rok.unique(),[dz.values[y][0] for y in range(len(dz.values))],color="orange", label="K", bottom=[ch.values[y][0] for y in range(len(ch.values))])
plt.xticks(df.Rok.unique(), rotation=45)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend()
plt.show()