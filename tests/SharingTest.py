#!/usr/bin/python3

import random
from deap import creator, base, tools, algorithms
from utilities import NormBinSeqToNum, PlotBinSeq, ScatBinFct, GenBinSeq
import matplotlib.pyplot as plt
from NichingMethods import Sharing
from distFunctions import NormHamming2, NichCluster
from statistics import mean
from FitFunctions import MaxMinEval, FnctA, FnctB, MaxFnctA, MaxFnctB
from benchmark import MaxPeakRatio, ChiSquareLike

# configure Individual size
IND_SIZE = 100
# configure num of individual
NUM_IND = 100
# configure max num of generations
NUM_GEN = 200
# configure the fitness function [FnctA, FnctB]
FitnessFunction = FnctA
# configure the corresponding set of PeackValues [MaxFnctA, MaxFnctB]
PeackValues = MaxFnctA
# configure selection method ['TR', 'SUS']
SelectMeth = 'SUS'
# configure ricombination method ['OneCx', 'StdUnifCx', 'TwoCx']
RecombMeth = 'StdUnifCx'
# configure the crossover probability
CxProbability = 1
# configure the Std-Uniform-Crossover probability.
StdUnifCxProb = 0.01
# configure the mutation probability
MxProbability = 0

# new class and attributes definition
creator.create("FitnShare", base.Fitness, weights=(1.0,))
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax, fitshare=creator.FitnShare, value=0)

# new methods definition for generate population
toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# new methods definition for run genetic algorithm
# fitness evaluation
toolbox.register("evalfit", FitnessFunction)
# fitness niching evaluation
toolbox.register("evalfitsh", Sharing, fit_funct=toolbox.evalfit, dist_funct=NormHamming2, share_radius=0.1)
# selection methods
if SelectMeth is 'TR':
    toolbox.register("select", tools.selTournament, tournsize=3, fit_attr='fitshare')
elif SelectMeth is 'SUS':
    toolbox.register("select", tools.selStochasticUniversalSampling, fit_attr='fitshare')
else:
    print("please chose a valid option")
# recombination methods
if RecombMeth is 'OneCx':
    toolbox.register("mate", tools.cxOnePoint)
elif RecombMeth is 'TwoCx':
    toolbox.register("mate", tools.cxTwoPoint)
elif RecombMeth is 'StdUnifCx':
    toolbox.register("mate", tools.cxUniform, indpb=StdUnifCxProb)
else:
    print("please chose a valid option")
# mutation method
toolbox.register("mutate", tools.mutFlipBit, indpb=MxProbability)

# benchmark comparison values
rapresentative=toolbox.population(n=len(PeackValues))
for ind,rap in zip(rapresentative,PeackValues):
    ind.value=rap[0]
    ind.fitness=rap[1]

# GAs initializzation
population = toolbox.population(n=NUM_IND)
MinFitness=[]
MaxFitness=[]
AvgFitness=[]
csq_dev=[]
mpr_val=[]

# GAs evaluation
for gen in range(NUM_GEN):
    # Mating
    offspring = algorithms.varAnd(population, toolbox, cxpb=CxProbability, mutpb=MxProbability)
    # Evaluation
    toolbox.evalfitsh(offspring)
    # Selection
    population = toolbox.select(offspring, k=len(population))

    for ind in population:
        ind.value=NormBinSeqToNum(ind)

    MinFitness.append(min([ind.fitness.values[0] for ind in population]))
    MaxFitness.append(max([ind.fitness.values[0] for ind in population]))
    AvgFitness.append(mean([ind.fitness.values[0] for ind in population]))

    csq_dev.append(ChiSquareLike(population, rapresentative, nich_radius=0.1))
    mpr_val.append(MaxPeakRatio(population, rapresentative))

# result section
print("Max Peak Ratio=", max(mpr_val))
print("Mean Chi-Square=", mean(csq_dev))
print("Max Chi-Square=", max(csq_dev)) 

# final plot results
plt.subplot(141)
plt.plot([i for i in range(NUM_GEN)],csq_dev)
plt.title('generation VS ChiSquareLike')
plt.xlabel('generation')
plt.ylabel('ChiSquareLike')
plt.grid(True)

plt.subplot(142)
plt.plot([i for i in range(NUM_GEN)],mpr_val)
plt.title('generation VS MaxPeakRatio')
plt.xlabel('generation')
plt.ylabel('MaxPeakRatio')
plt.grid(True)

plt.subplot(143)
num_gen=[i for i in range(NUM_GEN)]
plt.plot(num_gen, MaxFitness, 'r', label='MaxFitness')
plt.plot(num_gen, AvgFitness, 'g', label='AvgFitness')
plt.plot(num_gen, MinFitness, 'b', label='MinFitness')
plt.title('generation VS fitness')
plt.xlabel('generation')
plt.ylabel('Fitness')
plt.grid(True)
plt.legend()

# niches graphical rapresentation 
plt.subplot(144)
AllBinSeq = GenBinSeq(10)
AllPossibleFits = [FitnessFunction(i)[0] for i in AllBinSeq]
PlotBinSeq(AllBinSeq, AllPossibleFits, 'r')
ScatBinFct(population, FitnessFunction)
plt.title('fitness VS individuals')
plt.xlabel('Individuals')
plt.ylabel('Fitness')
plt.grid(True)

plt.show()
