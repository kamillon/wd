import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rzucaj(n):
    wynik = []
    for i in range(n):
        wynik.append(np.random.randint(1,7) + np.random.randint(1,7))
    plt.hist(wynik, bins=10, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Suma rzutów')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

rzucaj(1000)