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
