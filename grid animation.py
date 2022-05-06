"""
Created on Fri May  3 08:38:02 2022

@author: x
"""

import argparse  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.random import random, randint

def main(*args):
    parser = argparse.ArgumentParser(description='epidemic animation')
    parser.add_argument('--size', type=int, default=100)
    parser.add_argument('--duration', type=int, default=90)
    parser.add_argument('--recovery', type=float, default=0.1)
    parser.add_argument('--infection', type=float, default=0.67)
    #the inflection rate we estimated is0.67
    parser.add_argument('--death', type=float, default=0.0027)
    #the average death rate of UK ia about 0.27%
    parser.add_argument('--cases', type=int, default=2)
    parser.add_argument('--file', type=str, default=None)
    args = parser.parse_args(args)
    simulation = Simulation(args.size, args.size,
                            args.recovery, args.infection, args.death)
    simulation.infect_randomly(args.cases)
    animation = Animation(simulation, args.duration)
    if args.file is None:
            animation.show()
    else:
            animation.save(args.file)

class Simulation:
    susceptible = 0
    infected = 1
    recovered = 2
    dead = 3
    state = {'susceptible': susceptible,
             'infected': infected,
             'recovered': recovered,
             'dead': dead,}
    colour_map = {'susceptible': 'green',
              'infected': 'red',
              'recovered': 'blue',
              'dead': 'black', }
    map_colour_rgb = {'green': (0, 255, 0),
                  'red': (255, 0, 0),  
                  'blue': (0, 0, 255),
                  'black': (0, 0, 0),}

    def __init__(self, width, height, recovery, infection, death):
        self.day = 0
        self.width = width
        self.height = height
        self.recovery_probability = recovery
        self.infection_probability = infection
        self.death_probability = death
        self.state = np.zeros((width, height), int)
        self.state[:, :] = self.susceptible

    def infect(self, num):
        for n in range(num):
            x = randint(self.width)
            y = randint(self.height)
            self.state[x, y] = self.INFECTED

    def update(self):
        old_state = self.state
        new_state = old_state.copy()
        for x in range(self.width):
            for y in range(self.height):
                new_state[x, y] = self.get_new_status(old_state, x, y)
        self.state = new_state
        self.day += 1

    def get_new_state(self, state, x, y):
        position = state[x, y ]

        if position == self.INFECTED:
            if self.recovery_probability > random():
                return self.RECOVERED
            elif self.death_probability > random():
                return self.DEAD

        elif position == self.SUSCEPTIBLE:
            num = self.num_infected_around(state, x, y)
            if num * self.infection_probability > random():
                return self.INFECTED
            return position

    def num_infected_around(self, state, x, y):
        xvalues = range(max(x-1, 0), min(x+2, self.width))
        yvalues = range(max(y-1, 0), min(y+2, self.height))
        number = 0
        for xp in xvalues:
            for yp in yvalues:
                if (xp, yp) != (x, y):
                    if state[xp, yp] == self.INFECTED:
                        number += 1
        return number

    def get_rgb_matrix(self):
        rgb_matrix = np.zeros((self.width, self.height, 3), int)
        for status, statusnum in self.STATUSES.items():
            colour_name = self.colour_map[status]
            colour_rgb = self.map_colour_rgb[colour_name]
            rgb_matrix[self.state == statusnum] = colour_rgb
        return rgb_matrix

class Animation:
    def __init__(self, simulation, duration):
        self.simulation = simulation
        self.duration = duration

        self.figure = plt.figure(figsize=(8, 4))
        self.axes_grid = self.figure.add_subplot(1, 2, 1)

        self.gridanimation = GridAnimation(self.axes_grid, self.simulation)

    def show(self):
        animation = FuncAnimation(self.figure, self.update, frames=range(100),
                init_func = self.init, blit=True, interval=200)
        plt.show()

    def save(self, filename):
        animation = FuncAnimation(self.figure, self.update, frames=range(100),
                init_func = self.init, blit=True, interval=300)
        animation.save(filename, fps=30, extra_args=['-vcodec', 'libx264'])

    def init(self):
        actors = []
        actors += self.gridanimation.init()
        return actors

    def update(self, framenumber):
        self.simulation.update()
        actors = []
        actors += self.gridanimation.update(framenumber)
        return actors

class GridAnimation:

    def __init__(self, axes, simulation):
        self.axes = axes
        self.simulation = simulation
        rgb_matrix = self.simulation.get_rgb_matrix()
        self.image = self.axes.imshow(rgb_matrix)
        self.axes.set_xticks([])
        self.axes.set_yticks([])

    def init(self):
        return self.update(0)

    def update(self, framenum):
        day = framenum
        rgb_matrix = self.simulation.get_rgb_matrix()
        self.image.set_array(rgb_matrix)
        return [self.image]

sim = Simulation(10, 10,recovery=0.1, infection=0.67, death=0.027)
plt.show()
