import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

p = df.groupby(['Plec']).agg({"Liczba":["sum"]})
r = df.groupby(['Rok']).agg({"Liczba":["sum"]})
boys = df[df["Plec"]=='M'].groupby(['Rok']).sum()
girls = df[df["Plec"]=='K'].groupby(['Rok']).sum()

plt.subplot(1,3,1)
plt.bar(['K','M'],[p.values[0][0],p.values[1][0]],color=['red','blue'])
plt.ylabel('Ilosc urodzen (mln)')
plt.xlabel('Plec')

plt.subplot(1,3,2)
plt.plot(df.Rok.unique(),[boys.values[x][0] for x in range(len(boys.values))],"green", label="M")
plt.plot(df.Rok.unique(),[girls.values[x][0] for x in range(len(girls.values))],"orange", label="K")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilosc urodzen')
plt.xlabel('Rok')
plt.legend()

plt.subplot(1,3,3)
plt.bar(df.Rok.unique(),[r.values[x][0] for x in range(len(r.values))],color="c")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilosc urodzen')
plt.xlabel('Rok')
plt.show()