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

def Sharing(population, fit_funct, dist_funct, share_radius, shape_factor=1, scaling_factor=1):
    """ 
        The sharing techinque reduces the fitness of each individual proportionally at the population density of the belonging niche.
        The niche size is identify by the share radius parameter. This parameter encloses the information on the estimated distance between two peak.
    """
    for ind in population:
        niche = 0
        ind.fitness.values = fit_funct(ind)

        # evaluate the distance from the individual and the rest of population and update the niche factor
        for others in population:
            dist = dist_funct(ind, others)
            if dist < share_radius:
                niche = niche + ( 1 - (dist/share_radius)**shape_factor )
        
        # evaluate and assign the fit sharing value    
        ind.fitshare.values = ( (ind.fitness.values[0]**scaling_factor)/niche ),


def Clearing(population, fit_funct, dist_funct, clear_radius, niche_cap=5, attr_value="value"):
    # evaluate the fitness of each individual
    for ind in population:
        ind.fitness.values=fit_funct(ind)

    # each individual is assigned to a niche
    niches=NicheAssign(population, dist_funct, clear_radius, attr_value=attr_value)

    # fetch the best "niche_cap" individuals of each niche
    niche_leaders=[] # list of the best individuals in a niche
    super_ind=[]
    for subpop in niches:
        niche_leaders=tools.selBest(subpop, niche_cap)
        for supind in niche_leaders:
            super_ind.append(supind)
            
    # assign the fitness only to the best individual, reset the fitness of the others
    for ind,idx in zip(population,range(len(population))):
        if ind in super_ind:
            ind.fitclearing.values=ind.fitness.values
            population[idx].fitclearing.values=ind.fitness.values   # WARNIG : REPETE TWO TIMES THE SAME COMMAND!!!
        else:
            ind.fitclearing.values=0,

# New Clearing function: But less performance
def DummyClearing(population, fit_funct, dist_funct, clear_radius, niche_cap):

    # evaluate the fitness clearing
    for ind_idx in range(len(population)):
        # evaluate the fitness of the central_niche individual
        population[ind_idx].fitness.values=fit_funct(population[ind_idx])
        # List of best fitness individual, the list is sort by fitness value: [ [index 1, 0.12], ..., [index N, 0.92] ]
        BestNicheInd=[[0,0]]    

        for oth in range(len(population)):
            if dist_funct(population[ind_idx], population[oth])<clear_radius:
                population[oth].fitness.values=fit_funct(population[oth])   # You could verify if it is already update to not evaluate it again

                # evaluate if the individual has a best fitness
                if(population[oth].fitness.values[0]>BestNicheInd[0][1]):
                    if(len(BestNicheInd)>=niche_cap):
                        # reset the clearing fitness of the lest best ind in the BestNicheList if its fitness is less than a new individual of the niche
                        population[BestNicheInd.pop(0)[0]].fitclearing.values=0,   

                    # assign the clearing fitness
                    population[oth].fitclearing.values=population[oth].fitness.values 
                    BestNicheInd.append([oth,population[oth].fitness.values[0]])
                    BestNicheInd.sort(key=lambda tup: tup[1])                       
                else:
                    population[oth].fitclearing.values=0,   # reset the clearing fitness
               
        BestNicheInd.clear()