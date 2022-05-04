# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:37:34 2022

@author: Zecheng Yu  Russel
"""

def susceptible_plot():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    dB = pd.read_csv('./data.csv', sep = ',')

    S = dB['susceptible(S)']
    S = np.array(S)

    plt.plot(S)
    plt.xlabel('t')
    plt.title('Susceptible(S)')
    plt.show()

susceptible_plot()