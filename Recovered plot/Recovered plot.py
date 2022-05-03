# -*- coding: utf-8 -*-
"""
Created on Tue May  1 11:32:53 2022

@author：Yikai Zhang
"""

def recovered_plot():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    dB = pd.read_csv('./data.csv', sep = ',')

    R = dB['recovered(R)']
    R = np.array(R)

    plt.plot(R)
    plt.xlabel('t')
    plt.title('Recovered(R)')
    plt.show()

recovered_plot()