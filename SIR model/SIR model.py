# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 23:01:11 2022

@author: 李子安  Russel
"""

def SIR_model():
    from scipy.integrate import solve_ivp
    import numpy as np
    import matplotlib.pyplot as plt


    beta = 0.23
    gamma = 0.07
    def SIRode(t, y):
        return [-beta*y[0]*y[1], beta*y[0]*y[1] - gamma*y[1], gamma*y[1]]

    y0 = [.52, .24, .24]
    
    tspan = [0, 28]

    sol = solve_ivp(SIRode, tspan, y0,t_eval = np.linspace(0, 28,num=101))

    plt.plot(sol.t, sol.y.T)
    plt.legend(['susceptible', 'infected', 'recovered'], shadow=True)
    plt.xlabel('t')
    plt.title('SIR model')
    return

SIR_model()
