

class Guest:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setUnknownList(self, list):  #Initialise la liste des convives que le convive ne connait pas
        self.unknown = list[:]
        self.unknown.remove(self.id)

    def getUnknownList(self):
        return self.unknown

    def removeFromList(self, id):   #Retire les convives connus de cette liste
        self.known.remove(id)


    def constructLineWeight(self):
        lineWeight = "poids" + self.id + ": " + str(len(self.known)) + self.id
        for i in range(len(self.known)):
            lineWeight = lineWeight + " + " + self.known[i]
        lineWeight = lineWeight + " <= " + str(len(self.known))
        self.weight = lineWeight
        return lineWeight

    def getLenUnknown(self):
        return int(len(self.known))

    def addtoKnownList(self, item):
        self.known.add(item)

    def getKnownList(self):
        return self.known

    def setKnownList(self, list):
        self.known = list
    ## LP construction