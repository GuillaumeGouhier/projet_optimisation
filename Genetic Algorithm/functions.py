import random

def generateGenes():
    return [random.randint(0,1) for i in range(300)]

def initPop():
    population = [Solution() for i in range(0,100)]

    return population
