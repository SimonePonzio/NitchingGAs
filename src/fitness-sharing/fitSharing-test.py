#!/usr/bin/python

import random
from deap import algorithms, base, creator, tools

# define Individual size
IND_SIZE = 100

# classes creator: generate classes with a custom name inheriting other classes, eventually adding attributes and fixing parameters.
creator.create("IndFitness", base.Fitness, weights=(1.0,))      # create a class "FitnessMax" inheriting the class "base.Fitness" and initializing it.
creator.create("SharedFitness", base.Fitness, weights=(1.0,))      # create a class "FitnessMax" inheriting the class "base.Fitness" and initializing it.
creator.create("Individual", list, fitness=creator.IndFitness, sharFitness=creator.SharedFitness)  # create a class "Individual" inheriting the class "list" and adding one attribute.

# define the fitness fuction
def MaxAndMin(individual):
    return sum(individual),

# define the distance function as hamming distance
def NormHamming2(x,y):
    """Calculate the Hamming distance between two bit strings"""
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i]^y[i]:
            count=count+1
    return float(count)/float(len(x))

# evaluate the fitness sharing for all the population
def FitSharing(individual, pop, fitFunction, distanceFunction):
    sigma = 0.2
    alpha = 1
    nitche = 0
    fit = fitFunction(individual)
    print(fit)
    for others in pop:
        dist = distanceFunction(individual, others)
        if dist < sigma:
            nitche = nitche + ( 1 - (dist/sigma)**alpha )
    return(fit[0]/nitche)        

# declare and initialize a varible from class Toolbox
toolbox = base.Toolbox()

# use the register method of the Toolbox class in order to
toolbox.register("attr_bool", random.randint, 0, 1)                                             # register the method random.randint in a new method attr_bool. in this way attr_bool will generate a random integer in the range [0,1]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)   # the registered method "individual" will lunch the function "attr_bool" defined on the line above 100 times, filling the class "Individual" (it is a list)    
toolbox.register("population", tools.initRepeat, list, toolbox.individual)                      # the registered method "population" will lunch the method "toolbox.individual" n time generating a variable of type 'list'

population = toolbox.population(n=10)
print(population)

# the registered method "evaluate" will lunch the function evalOneMax 
toolbox.register("evaluate", FitSharing, pop=population, fitFunction=MaxAndMin, distanceFunction=NormHamming2)  

ShareFit = toolbox.evaluate(population[0])

print(ShareFit)    