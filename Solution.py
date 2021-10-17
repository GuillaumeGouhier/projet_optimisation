import random
class Solution(object):
    """docstring for Solution."""

    def __init__(self, genes = []):
        super(Solution, self).__init__()
        if len(genes) == 0:
            genes = generateGenes()
        self.genes = genes

    def generateGenes ():
        return [random.randint(0, 1) for i in range(300)]
## TODO: Check If Solution Is Viable
    def updatePossible(self):
        self.isPossible = False
        #If possible, then everyone knows each other.
        # == len knownSet U candidate
        liste_candidate = [i for i in range(len(self.genes)) if self.genes[i] == 1]
        checkLen = ()
        for i in self.genes:
            checkLen.add(len(list(filter(lambda x: x.getId() in item.getKnownList(), liste_candidate))))

        #If everyone knows eachother, then set of known people should be equal in whole candidate liste
        return len(checkLen) == 1
    def mutate(self, proba):
        self.genes = list(map(lambda x : 1 - x if random.random() <= proba else x, self.genes))
        return 0

    def repair (self, data):
        # Repair phase to ensure every child solution can live
        invites_candidate = [i for i in range(len(self.genes)) if self.genes[i] == 1]
        # Map invite to score
        scores = list(map(lambda x: (len([j for j in invites_candidate if j not in data[x].getKnownList()]), x), invites_candidate).sort(reverse=True))
        # Remove if too problematic
        i = 0
        while self.isPossible == False:
            self.genes[invites_candidate[scores[i][1]]] = 0
            i=i+1
            #Update Possible State
            self.updatePossible()
        # Till everyone knows everyone
