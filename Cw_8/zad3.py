import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
df = pd.read_csv('zamowienia.csv', header = 0, sep = ";")

# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
def a():
    print(df['Sprzedawca'].unique())

# 5 najwyższych wartości zamówień
def b():
   print(df.sort_values(by='Utarg').tail(5))

# ilość zamówień złożonych przez każdego sprzedawcę
def c():
    print(df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']}))

# sumę zamówień dla każdego kraju
def d():
    print(df.groupby(['Kraj']).agg({"idZamowienia":['count']}))

# sumę zamówień dla roku 2005, dla sprzedawców z Polski
def e():
    print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01')
         & (df['Data zamowienia'] <= '2005-12-31')].agg({'idZamowienia': ['count']}))

# średnią kwotę zamówienia w 2004 roku
def f():
    print(df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')].agg({'Utarg':['mean']}))

# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
def g():
    d1 = df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')]
    d1.to_csv('D:\wiz_repo\wd\Cw_8\zamowienia_2004.csv', header=None, index=False)
    d2 = df[(df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')]
    d2.to_csv('D:\wiz_repo\wd\Cw_8\zamowienia_2005.csv', header=None, index=False)

a()
b()
c()
d()
e()
f()
g()