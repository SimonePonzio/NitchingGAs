#!/usr/bin/python3

import random
from deap import algorithms, base, creator, tools
from prettytable import PrettyTable

# define Individual size
IND_SIZE = 10
# define the population size
NUM_IND = 10

# classes creator: generate classes with a custom name inheriting other classes, eventually adding attributes and fixing parameters.
creator.create("IndFitness", base.Fitness, weights=(1.0,))      # create a class "FitnessMax" inheriting the class "base.Fitness" and initializing it.
creator.create("SharedFitness", base.Fitness, weights=(1.0,))      # create a class "FitnessMax" inheriting the class "base.Fitness" and initializing it.
creator.create("Individual", list, fitness=creator.IndFitness, sharFitness=creator.SharedFitness)  # create a class "Individual" inheriting the class "list" and adding one attribute.

# define the fitness fuction
def MaxAndMin(individual):
    negInd=list(map(int,[not i for i in list(map(bool,individual))]))
    return max( (sum(individual),) , (sum(negInd),) )

# define the distance function as hamming distance
def NormHamming2(x,y):
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i]^y[i]:
            count=count+1
    return float(count)/float(len(x))

# evaluate the fitness sharing for all the population
def FitSharing(individual, pop, fitFunction, distanceFunction):
    sigma = 0.4
    alpha = 1
    nitche = 0
    fit = fitFunction(individual)
    for others in pop:
        dist = distanceFunction(individual, others)
        if dist < sigma:
            nitche = nitche + ( 1 - (dist/sigma)**alpha )
    return((fit[0]/nitche),nitche)        

# declare and initialize a varible from class Toolbox
toolbox = base.Toolbox()

# use the register method of the Toolbox class in order to
toolbox.register("attr_bool", random.randint, 0, 1)                                             # register the method random.randint in a new method attr_bool. in this way attr_bool will generate a random integer in the range [0,1]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)   # the registered method "individual" will lunch the function "attr_bool" defined on the line above 100 times, filling the class "Individual" (it is a list)    
toolbox.register("population", tools.initRepeat, list, toolbox.individual)                      # the registered method "population" will lunch the method "toolbox.individual" n time generating a variable of type 'list'

# define the pulation
population = toolbox.population(n=NUM_IND)

# genera una lista di stringhe così: [Ind1, Ind2, Ind3, ...]
IndNames = ['Ind'+str(i+1) for i in range(NUM_IND)]

# the registered method "EvalFitness" evaluate the Fitness 
toolbox.register("EvalFitness", MaxAndMin) 

# the registered method "EvalShareFit" evaluate the Fitness Sharing 
toolbox.register("EvalShareFit", FitSharing, pop=population, fitFunction=MaxAndMin, distanceFunction=NormHamming2)  


result = [toolbox.EvalShareFit(population[i]) for i in range(NUM_IND)]
ShareFit = [result[i][0] for i in range(NUM_IND)]
Nitche = [result[i][1] for i in range(NUM_IND)]

IndNames=list(map(str,IndNames))
ShareFit=list(map(str,ShareFit))
Nitche=list(map(str,Nitche))

IndNames.insert(0,'Names')
ShareFit.insert(0,'ShareFit')
Nitche.insert(0,'Nitche')

t = PrettyTable(IndNames)
t.add_row(ShareFit)
t.add_row(Nitche)

print(t)
