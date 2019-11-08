#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import BarBinFct, BarBinSeq, GenBinSeq, PlotBinSeq
import matplotlib.pyplot as plt
from fitsharing import FitSharing, NormHamming2
from statistics import mean

# define Individual size
IND_SIZE = 100
# define num of individual
NUM_IND = 200
# define max num of generations
MAX_NUM_GEN = 30

creator.create("FitnShare", base.Fitness, weights=(1.0,))
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax, fitshare=creator.FitnShare)

toolbox = base.Toolbox()

def MaxMinEval(individual):
    negInd=list(map(int,[not i for i in list(map(bool,individual))]))
    return max( (sum(individual)) , (sum(negInd)) ),

def evalOneMax(individual):
    return sum(individual),

toolbox.register("evalfit", MaxMinEval)
toolbox.register("evalfitsh", FitSharing, fitFunction=toolbox.evalfit, distanceFunction=NormHamming2)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# AllBinSeq = GenBinSeq(IND_SIZE)
# AllPossibleFits = [MaxMinEval(i)[0] for i in AllBinSeq]

MinFitness=[]
MaxFitness=[]
AvgFitness=[]

for num_gen in range(MAX_NUM_GEN):
    population = toolbox.population(n=NUM_IND)

    for gen in range(num_gen):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.01)
        for ind in offspring:
            ind.fitshare.values = toolbox.evalfitsh(ind, offspring)
        population = toolbox.select(offspring, k=len(population))

    FitnessValues=list([toolbox.evalfit(i)[0] for i in population])
    MinFitness.append(min(FitnessValues))
    MaxFitness.append(max(FitnessValues))
    AvgFitness.append(mean(FitnessValues))

# print("Min Fintness per gen = ", MinFitness)
# print("Max Fintness per gen = ", MaxFitness)
# print("Avg Fintness per gen = ", AvgFitness)

num_gen=[i for i in range(MAX_NUM_GEN)]
plt.plot(num_gen, MinFitness, 'b', label='MinFitness')
plt.plot(num_gen, MaxFitness, 'r', label='MaxFitness')
plt.plot(num_gen, AvgFitness, 'g', label='AvgFitness')
plt.title('generation VS fitness')
plt.xlabel('generation')
plt.ylabel('Fitness')
plt.grid(True)
plt.legend()

plt.show()