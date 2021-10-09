

class Glouton:

    def __init__(self, id, poids):
        self.id = id
        self.nb_connaissance = poids

    def getId(self):
        return self.id

    def getNbConnaissance(self):
        return self.nb_connaissance

    def critere_choix(self, poids, id, id_temp, var_temp):
        if int(poids) <= int(var_temp):
            return Glouton(id, poids)
        else:
            return Glouton(id_temp, var_temp)

