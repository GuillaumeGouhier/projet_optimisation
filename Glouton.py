

class Glouton:

    def __init__(self, id, weight):
        self.id = id
        self.nb_relationship = weight

    def getId(self):
        return self.id

    def getNbRelationship(self):
        return self.nb_relationship

    def criteria_choice(self, weight, id, id_temp, var_temp):
        if int(weight) <= int(var_temp):
            return Glouton(id, weight)
        else:
            return Glouton(id_temp, var_temp)

