

class Convive:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setlisteNonConnu(self, liste):  #Initialise la liste des convives que le convive ne connait pas
        self.nonConnu = liste[:]
        self.nonConnu.remove(self.id)

    def removeFromList(self, id):   #Retire les convives connus de cette liste
        self.nonConnu.remove(id)


    def constructPoids(self):
        poids = "poids" + self.id + ": " + str(len(self.nonConnu)) + self.id
        for i in range(len(self.nonConnu)):
            poids = poids + " + " + self.nonConnu[i]
        poids = poids + " <= " + str(len(self.nonConnu))
        return poids