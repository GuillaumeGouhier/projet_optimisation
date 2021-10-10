

class Convive:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setlisteConnu(self, liste):  #Initialise la liste des convives que le convive ne connait pas
        self.connu = liste[:]
        self.connu.remove(self.id)

    def getListeConnu(self):
        return self.connu

    def removeFromList(self, id):   #Retire les convives connus de cette liste
        self.connu.remove(id)


    def constructPoids(self):
        poids = "poids" + self.id + ": " + str(len(self.connu)) + self.id
        for i in range(len(self.connu)):
            poids = poids + " + " + self.connu[i]
        poids = poids + " <= " + str(len(self.connu))
        self.weight = poids
        return poids

    def getLenConnu(self):
        return int(len(self.connu))
