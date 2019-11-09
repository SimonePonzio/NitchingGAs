#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
import utilities as utils
import FitFunctions as fct

# define Individual size
IND_SIZE = 6
# define the population size
NUM_IND = 8

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

population = toolbox.population(n=NUM_IND)

utils.plt.subplot(121)
utils.PlotBinFct(utils.GenBinSeq(6), fct.OneMaxEval, 'r')
utils.ScatBinFct(population, fct.OneMaxEval)

utils.plt.subplot(122)
utils.BarBinFct(utils.GenBinSeq(6), fct.OneMaxEval)
utils.BarBinFct(population, fct.OneMaxEval)

utils.plt.show()
