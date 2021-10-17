class Convive:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setUnknownList(self, list):  # Initialise la liste des convives que le convive ne connait pas
        self.unknown = list[:]
        self.unknown.remove(self.id)

    def removeFromList(self, id):  # Retire les convives connus de cette liste
        self.unknown.remove(id)

    def constructLineWeight(self):
        lineWeight = "poids" + self.id + ": " + str(len(self.unknown)) + self.id
        for i in range(len(self.unknown)):
            lineWeight = lineWeight + " + " + self.unknown[i]
        lineWeight = lineWeight + " <= " + str(len(self.unknown))
        self.weight = lineWeight
        return lineWeight

