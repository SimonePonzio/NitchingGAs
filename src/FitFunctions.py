#!/usr/bin/python3

def MaxMinEval(individual):
    negInd=list(map(int,[not i for i in list(map(bool,individual))]))
    return max( (sum(individual)) , (sum(negInd)) ),

def OneMaxEval(individual):
    return sum(individual),