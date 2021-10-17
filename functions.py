import random
from Solution import Solution

def initPop(size, data):
    population = [Solution() for i in range(0,size)]
    for i in population:
        i.repair(data)
    return population

## TODO: Support for multiple genetic ( random etc)
def breed(parent1, parent2):

    child1 = Solution([parent1.getGenes()[:150]] + parent2.getGenes()[150:])
    child2 = Solution([parent2.getGenes()[:150]] + parent1.getGenes()[150:])

    return child1, child2

def mutation(proba, population):
    return list(map(lambda x: x.mutate(proba), population))

def parentCouples(population):

    random.shuffle(population)

    couples = [(population[i], population[i+1]) for i in range(0, len(population), 2)]

    return couples

def addChilds(couples):

    return list(map(lambda x: breed(x[0], x[1]), couples))

def select_survivors(population):
    print(population)
    print(list(map(lambda x: x.getisPossible(), population)))
    return list(filter(lambda x: x.getisPossible(), population))


def bestscore(population):
    return max(list(map(lambda x: x.getScore(), population)))

# TODO: going from genX to genX+1
def nextGeneration(population):
    print(len(population))
    survivors = select_survivors(population)
    survivors.extend(addChilds(parentCouples(population)))
    return survivors
