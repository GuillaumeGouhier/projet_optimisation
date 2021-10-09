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

def mutation(proba, solution):
    if(random.random() <= proba):
        solution.mutate()

def parentCouples():

    couples = random.shuffle()

def nextPop(population):
    return list(filter(lambda x: x.isPossible(), population))
