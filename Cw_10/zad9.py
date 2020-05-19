import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv', header=0, sep = ";")

p = df.groupby(['Sprzedawca']).agg({"idZamowienia":['count']})
sprzedawcy = p.index.values
zamowienia = [p.values[y][0] for y in range(len(p.values))]
Explode = [0 for i in range(len(p.index.values))]
Explode[2]=0.1
plt.figure(figsize=(10,6))

wedges, texts, autotexts = plt.pie(zamowienia, explode=Explode, shadow=True, labels=sprzedawcy,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))
plt.setp(autotexts, size=10, weight="bold")
plt.legend(title='Sprzedawcy', loc='best', bbox_to_anchor=(1.5,1))
plt.show()