import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
df=pd.read_csv('iris.data',delimiter=",",header=None)

groups = df.groupby(4)
for name, group in groups:
    plt.plot(group[0], group[1], marker="o", linestyle="", label=name)
plt.legend()
plt.show()

