#!/usr/bin/python3

from numpy import arange

# return the normalize hamming distance
def NormHamming2(x,y):
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i]^y[i]:
            count=count+1
    return float(count)/float(len(x))

# def MatrixDist(pop, dist_funct=NormHamming2):
#     for i in range(len(pop)/2)
#         pop.dist

def FloatDist(x,y):
    return abs(x - y)

def BestMatch(population, goal_ind, dist_funct=FloatDist):
    dist_ind = [(dist_funct(goal_ind.value, individual.value)) for individual in population]
    BestInd = population[dist_ind.index(min(dist_ind))]
    return BestInd

def NichCluster(population, rapresentative, dist_funct=FloatDist, nich_radius=0.1, attr_value="value"):
    # WARNING: need to insert a control machanism on the overlap between vip area - the overlap is forbidden!

    # define vip areas
    vip_areas=[[getattr(vip, attr_value)-nich_radius,getattr(vip, attr_value)+nich_radius] for vip in rapresentative]
    niches=[ [] for i in range(len(vip_areas)+1) ]    

    # assign each individual to a vip area or to the non-vip area it it doesn't match with any vip area
    for ind in population:
        is_assigned=False
        for vip_zone,idx in zip(vip_areas,range(len(vip_areas)+1)):
            if min(vip_zone) <= getattr(ind, attr_value) <= max(vip_zone):
                niches[idx].append(ind)
                is_assigned=True
                break
        if (is_assigned==False):
            niches[len(vip_areas)].append(ind)
            is_assigned=False
            
    return niches

def NicheAssign(population, dist_funct, clear_radius, attr_value="value"):
    # define vip areas
    # num_niches = 1/(2*clear_radius)
    nich_areas=[ [i-clear_radius, i+clear_radius] for i in arange(clear_radius,1+clear_radius,(clear_radius*2))]
    niches=[ [] for i in range(len(nich_areas)) ]

    # assign each individual to a vip area or to the non-vip area it it doesn't match with any vip area
    for ind in population:
        is_assigned=False
        for vip_zone,idx in zip(nich_areas,range(len(nich_areas)+1)):
            if min(vip_zone) <= getattr(ind, attr_value) <= max(vip_zone):
                niches[idx].append(ind)
                is_assigned=True
                break
        if (is_assigned==False):
            niches[len(vip_areas)].append(ind)
            is_assigned=False

    return niches