import pandas as pd
import numpy as np
import xlrd
import openpyxl

pd.set_option('display.max_rows', None)
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')

# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
def a():
    print(df[df['Liczba'] > 1000])

# tylko rekordy gdzie nadane imię jest takie jak Twoje
def b():
    print(df[df['Imie'] == "KAMIL"])

# sumę wszystkich urodzonych dzieci w całym danym okresie
def c():
    print(df.agg({"Liczba":["sum"]}))

# sumę dzieci urodzonych w latach 2000-2005
def d():
    s=df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
    print(s.agg({"Liczba":['sum']}))

# sumę urodzonych chłopców i dziewczynek
def e():
    print(df[df['Plec'] == "M"].agg({'Liczba': [sum]}))
    print(df[df['Plec'] == "K"].agg({'Liczba': [sum]}))

# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
def f():
    print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))

# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie
def g():
    print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[[0, 1]])

a()
b()
c()
d()
e()
f()
g()


