# -*- coding: utf-8 -*-
"""
Created on Tue May  3 00:21:57 2022

@author: Zecheng Yu  Russel
"""

def infected_plot():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    dB = pd.read_csv('./data.csv', sep = ',')

    I = dB['infected(I)']
    I = np.array(I)

    plt.plot(I)
    plt.xlabel('t')
    plt.title('Infected(I)')
    plt.show()

infected_plot()