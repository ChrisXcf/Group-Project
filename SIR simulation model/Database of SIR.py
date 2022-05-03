# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:14:08 2022

@author: 李子安  Russel
"""
def database_of_SIR():
    
    import pandas as pd

    dB = pd.read_csv('./data.csv', sep = ',')
    return dB

    
print(database_of_SIR())