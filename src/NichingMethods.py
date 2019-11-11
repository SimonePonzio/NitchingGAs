#!/usr/bin/python3

from deap import tools
from distFunctions import NicheAssign

def FitSharing(individual, pop, fitFunction, distanceFunction, sigma=0.2, shape=1, scaling=1):
    niche = 0
    fit = fitFunction(individual)
    for others in pop:
        dist = distanceFunction(individual, others)
        if dist < sigma:
            niche = niche + ( 1 - (dist/sigma)**shape )
    return((fit[0]**scaling)/niche),

def Sharing(population, fitFunction, distanceFunction, sigma=0.2, shape=1, scaling=1):
    for ind in population:
        niche = 0
        ind.fitness.values = fitFunction(ind)
        for others in population:
            dist = distanceFunction(ind, others)
            if dist < sigma:
                niche = niche + ( 1 - (dist/sigma)**shape )
            ind.fitsharing.values = (ind.fitness.values**scaling)/niche

def Clearing(population, fit_funct, dist_funct, clear_radius=0.1, niche_cap=5, attr_value="value"):
    # evaluate the fitness of each individual
    for ind in population:
        ind.fitness.values=fit_funct(ind)

    # each individual is assigned to a niche
    niches=NicheAssign(population, dist_funct, clear_radius, attr_value=attr_value)

    # fetch the best "niche_cap" individuals of each niche
    niche_leaders=[] # list of the best individuals in a niche
    SoN = 0 # Start of Niche (SoN) - End of Niche (EoN)
    super_ind=[]
    for subpop in niches:
        niche_leaders=tools.selBest(subpop, niche_cap)
        for supind in niche_leaders:
            super_ind.append(supind)
            
    # assign the fitness only to the best individual, reset the fitness of the others
    for ind,idx in zip(population,range(len(population))):
        if ind in super_ind:
            ind.fitclearing.values=ind.fitness.values
            population[idx].fitclearing.values=ind.fitness.values
        else:
            ind.fitclearing.values=0,