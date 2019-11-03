#!/usr/bin/python3

import random
from deap import algorithms, base, creator, tools

# define Individual size
IND_SIZE = 10

# classes creator: generate classes with a custom name inheriting other classes, eventually adding attributes and fixing parameters.
creator.create("Individual", list)

def NormHamming2(x,y):
    """Calculate the Hamming distance between two bit strings"""
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i]^y[i]:
            count=count+1
    print(count)
    return count/len(x)

# declare and initialize a varible from class Toolbox
toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)                                             
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)

indA = toolbox.individual()
print(indA)
indB = toolbox.individual()
print(indB)

ham = NormHamming2(indA, indB)
print(ham)