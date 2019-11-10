#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import PlotBinSeq, ScatBinFct, GenBinSeq, NormBinSeqToNum
from matplotlib import pyplot as plt
from matplotlib import animation
from NitchingMethods import FitSharing
from distFunctions import NormHamming2
from FitFunctions import FnctA, FnctB
import numpy as np

"""
still not working
"""

# define Individual size
IND_SIZE = 12
# define num of individual
NUM_IND = 100
# define num of generations
NUM_GEN = 4
# define the fitness function between [FnctA, FnctB]
FitnessFunction = FnctA

creator.create("FitnShare", base.Fitness, weights=(1.0,))
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax, fitshare=creator.FitnShare)

toolbox = base.Toolbox()

toolbox.register("evalfit", FitnessFunction)
toolbox.register("evalfitsh", FitSharing, fitFunction=toolbox.evalfit, distanceFunction=NormHamming2, sigma=0.2)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selStochasticUniversalSampling, fit_attr='fitshare')
# toolbox.register("select", tools.selTournament, tournsize=3, fit_attr='fitshare')

population = toolbox.population(n=NUM_IND)

AllBinSeq = GenBinSeq(IND_SIZE)
AllPossibleFits = [FitnessFunction(i)[0] for i in AllBinSeq]
NumSequences=[NormBinSeqToNum(i) for i in AllBinSeq]

fig, ax = plt.subplots()
ax.plot(NumSequences, AllPossibleFits, '-r')
scatt = ax.scatter([NormBinSeqToNum(i) for i in population],[FitnessFunction(i)[0] for i in population])

def animate(frame, population=population, toolbox=toolbox):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.1, mutpb=0)
    for ind in offspring:
        ind.fitshare.values = toolbox.evalfitsh(ind, offspring)
    population = toolbox.select(offspring, k=len(population))
    xdata=np.asarray([NormBinSeqToNum(i) for i in population])
    ydata=np.asarray([FitnessFunction(i)[0] for i in population])
    scatt.set_array(np.c_(xdata,ydata))

ani = animation.FuncAnimation(fig, animate, frames=[i for i in range(NUM_GEN)], blit=True)

plt.show()