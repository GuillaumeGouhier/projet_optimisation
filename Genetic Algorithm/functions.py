import random

def generateGenes():
    return [random.randint(0,1) for i in range(300)]

def initPop():
    population = [Solution() for i in range(0,100)]

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
    return list(filter(lambda x: x.isPossible(), population))


def bestscore(population):
    return max(list(map(lambda x: x.getScore(), population)))

# TODO: going from genX to genX+1
def nextGeneration(population):
    survivors = select_survivors(population)
    survivors.add(addChilds(parentCouples(population)))
    return survivors
