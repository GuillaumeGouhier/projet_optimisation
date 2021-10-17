import random
class Solution(object):
    """docstring for Solution."""

    def __init__(self, genes = []):
        super(Solution, self).__init__()
        self.isPossible = False
        self.genes = genes
        if len(genes) == 0:
            self.generateGenes()

    def generateGenes (self):
        self.genes =  [random.randint(0, 1) for i in range(300)]
## TODO: Check If Solution Is Viable
    def updatePossible(self):
        #If possible, then everyone knows each other.
        # == len knownSet U candidate
        liste_candidate = [i for i in range(len(self.genes)) if self.genes[i] == 1]
        checkLen = set()
        for i in self.genes:
            checkLen.add(len(list(filter(lambda x: x.getId() in item.getKnownList(), liste_candidate))))

        #If everyone knows eachother, then set of known people should be equal in whole candidate liste
        self.isPossible = len(checkLen) == 1

    def mutate(self, proba):
        self.genes = list(map(lambda x : 1 - x if random.random() <= proba else x, self.genes))
        return 0

    def repair (self, data):
        # Repair phase to ensure every child solution can live
        invites_candidate = set()
        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                invites_candidate.add(i)
        print("Candidats: ", invites_candidate)
        # Map invite to score
        ##Debug
        print(len(data[list(invites_candidate)[0]].getKnownList().difference(invites_candidate)))

        scores = list()
        for i in invites_candidate:
            scores.append(len(data[i].getKnownList().difference(invites_candidate)))
        print(scores)
        # Remove if too problematic
        while self.isPossible == False:
            self.genes[scores[0]] = 0
            i=i+1
            #Update Possible State
            self.updatePossible()
        # Till everyone knows everyone

    def getGenes(self):
        return self.genes

    def getisPossible(self):
        return self.isPossible

    def K_Flip(self, k):  # Create a new solution with 3 flipped gene
        tab_rand = []
        new_gene = self.genoa.copy()
        dejaUtilise = 0
        for i in range(k):
            randnumber = randint(0, len(self.genoa))
            for j in range(tab_rand):
                if randnumber == tab_rand[j]:
                    dejaUtilise = 1
            if dejaUtilise == 0:
                tab_rand.append(randnumber)
                new_gene[randnumber] = 1 - new_gene[randnumber]
            else:
                i = i - 1

        return (Solution(new_gene))