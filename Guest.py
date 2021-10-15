

class Guest:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setKnownList(self, list):  #Initialise la liste des convives que le convive ne connait pas
        self.known = list[:]
        self.known.remove(self.id)

    def getKnownList(self):
        return self.known

    def removeFromList(self, id):   #Retire les convives connus de cette liste
        self.known.remove(id)


    def constructLineWeight(self):
        lineWeight = "poids" + self.id + ": " + str(len(self.known)) + self.id
        for i in range(len(self.known)):
            lineWeight = lineWeight + " + " + self.known[i]
        lineWeight = lineWeight + " <= " + str(len(self.known))
        self.weight = lineWeight
        return lineWeight

    def getLenKnown(self):
        return int(len(self.known))

    def liste_candidate(self, list):
        self.known = list[:]
        self.known.remove(self.id)

