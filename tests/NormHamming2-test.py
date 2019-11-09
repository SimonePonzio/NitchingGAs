#!/usr/bin/python3

import random
from deap import algorithms, base, creator, tools
from distFunctions import NormHamming2

# define Individual size
IND_SIZE = 10

# classes creator: generate classes with a custom name inheriting other classes, eventually adding attributes and fixing parameters.
creator.create("Individual", list)

# declare and initialize a varible from class Toolbox
toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)                                             
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=IND_SIZE)

indA = toolbox.individual()
print("Individual A = ", indA)
indB = toolbox.individual()
print("Individual B = ", indB)

ham = NormHamming2(indA, indB)
print("Normalize Hamming distance = ", ham)