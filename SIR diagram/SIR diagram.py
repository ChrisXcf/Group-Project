# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:37:16 2022

@author: 李子安  Russel
"""

def SIR_diagram():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    dB = pd.read_csv('./data.csv', sep = ',')

    S = dB['susceptible(S)']
    S = np.array(S)

    I = dB['infected(I)']
    I = np.array(I)

    R = dB['recovered(R)']
    R = np.array(R)

    plt.plot(S)
    plt.plot(I)
    plt.plot(R)
    plt.legend(['susceptible', 'infected', 'recovered'], shadow=True)
    plt.xlabel('t')
    plt.title('SIR diagram')

SIR_diagram()


