class Solution(object):
    """docstring for Solution."""

    def __init__(self, genes):
        super(Solution, self).__init__()
        self.genes = genes

## TODO: Check If Solution Is Viable
    def isPossible(self):
        return True

    def mutate(self, proba):
        self.genes = list(map(lambda x : 1-x if random.random() <= proba else x, self.genes ))
        return 0

    def repair (self, data):
        # Repair phase to ensure every child solution can live
        invites_candidate = [i for i in range(len(self.genes)) if self.genes[i]==1 ]
        # Map invite to score
        scores = list(map(lambda x: (len([j for j in invites_candidate if j not in data[x].getListeConnu()]), x), invites_candidate).sort(reverse=True)
        # Remove if too problematic
        while !self.isPossible():
            self.genes[invites_candidate[scores[i][1]]] = 0
        # Till everyone knows everyone
        
