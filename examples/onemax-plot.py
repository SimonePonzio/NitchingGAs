#!/bin/python3

import random
from deap import algorithms, base, creator, tools

# plot stuff

import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rcParams['text.latex.preamble'] ='\\usepackage{libertine}\n\\usepackage[utf8]{inputenc}'

# more plot stuff
# import seaborn
# seaborn.set(style='whitegrid')
# seaborn.set_context('notebook')

# classes creator: generate classes with a custom name inheriting other classes, eventually adding attributes and fixing parameters.
creator.create("FitnessMax", base.Fitness, weights=(1.0,))      # create a class "FitnessMax" inheriting the class "base.Fitness" and initializing it.
creator.create("Individual", list, fitness=creator.FitnessMax)  # create a class "Induvidual" inheriting the class "list" and adding one attribute.

# define the fitness fuction
def evalOneMax(individual):
    return (sum(individual),)

# declare and initialize a varible from class Toolbox
toolbox = base.Toolbox()

# use the register method of the Toolbox class in order to
toolbox.register("attr_bool", random.randint, 0, 1)                                             # register the method random.randint in a new method attr_bool. in this way attr_bool will generate a random integer in the range [0,1]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=100)  # the registered method "individual" will lunch the function "attr_bool" defined on the line above 100 times, filling the class "Individual" (it is a list)    
toolbox.register("population", tools.initRepeat, list, toolbox.individual)                      # the registered method "population" will lunch the method "toolbox.individual" n time generating a variable of type 'list'

toolbox.register("evaluate", evalOneMax)                        # the registered method "evaluate" will lunch the function evalOneMax 
toolbox.register("mate", tools.cxTwoPoint)                      # the registered method "mate" will lunch the method "tools.cxTwoPoint"
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)        # the registered method "mutate" will lunch the method "tools.mutFlipBit" and will fix the second argument of the method (porbability of each attribute to flip)
toolbox.register("select", tools.selTournament, tournsize=3)    # the registered method "select" will lunch the methot "selTournament" and fix the argument tournsize = 3 -> look at "selTournament" for more info.

"""
START OF EXPERIMENT
"""

# generate a population of 300 "Individual", each of them is a list off 100 random numbers in the range [0,1]
pop = toolbox.population(n=300)

# compute for ngen times the new generation, evaluating the previous one. It uses the methods defined in lines [34 to 37] and it needs this names in order to work correctly.
result = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, verbose=False) # NGEN = 10
# print results
print('Current best fitness:', evalOneMax(tools.selBest(pop, k=1)[0]))

# compute for ngen times the new generation, evaluating the previous one. It uses the methods defined in lines [34 to 37] and it needs this names in order to work correctly.
result = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=50, verbose=False) # NGEN = 50
# print results
print('Current best fitness:', evalOneMax(tools.selBest(pop, k=1)[0]))