import sys
from Guest import Guest

if __name__ == '__main__':
    if len(sys.argv) > 2:
        source_file = open(sys.argv[1], "r")
        destination_file = open(sys.argv[2], "w")

        source_data = source_file.readline()
        source_data = source_data.split()

        print(source_data)
        binaries_list = []
        guest_list = []
        destination_file.write("Maximize" + '\n')
        z_max = "z: "

        for i in range(int(source_data[0])):
            coeff_i = source_file.readline().strip().split()

            z_max = z_max + coeff_i[1] + " x" + coeff_i[0] + " + "

            binaries_list.append("x" + coeff_i[0])
            guest_list.append(Guest("x" + coeff_i[0]))
        print(binaries_list)

        for i in range(len(guest_list)):
            guest_list[i].setKnownList(binaries_list)
        print(binaries_list)

        z_max = z_max[:-2]
        print(z_max)

        destination_file.write(z_max + '\n')
        destination_file.write("Subject To" + '\n')
        for i in range(int(source_data[1])):  # Construction des liens entre les convives ne se connaissant pas
            lien_i_j = source_file.readline().strip().split()

            lien_i_j[0] = "x" + lien_i_j[0]
            lien_i_j[1] = "x" + lien_i_j[1]
            for j in range(len(guest_list)):
                if lien_i_j[0] == guest_list[j].getId():
                    guest_list[j].removeFromList(lien_i_j[1])
                if lien_i_j[1] == guest_list[j].getId():
                    guest_list[j].removeFromList(lien_i_j[0])

        print(guest_list[0].constructLineWeight())

        for i in range(len(guest_list)):
            destination_file.write(guest_list[i].constructLineWeight() + '\n')

        destination_file.write("binaries \n")

        for i in range(len(guest_list)):
            destination_file.write(guest_list[i].getId() + '\n')

        destination_file.write("End")
        source_file.close()
        destination_file.close()
    else:
        print("Utilisation : python main.py source.txt destination.lp")


# final_list = liste d'ID
# candidate_list = liste de Convives

##Critère basé sur le nombre de relations pour tenter de maximiser le score. Mais pas le score directement

def recursiveGlouton(candidate_list, final_list):
    print("\n Candidate list: ", candidate_list)
    print("\n Final list: ", final_list)
    # Compter nb personnes connues
    max_so_far = 0
    next_candidate = -1
    # Future liste candidate
    tmp_liste = []
    # Permet de savoir si tous se connaissent
    checkLen = ()

    for item in candidate_list:

        tmp = list(filter(lambda x: x.getId() in item.getKnownList(), candidate_list))
        checkLen.add(len(tmp))
        # Algo pour garder le meilleur candidat ( Nb de relations connues)
        if max_so_far < len(tmp):
            tmp_liste = tmp
            max_so_far = len(tmp)
            next_candidate = item.getId()

    # Renvoie la liste d'ID des Convives
    if (len(checkLen) == 1):
        return final_list

    final_list.add(next_candidate)
    candidate_list = tmp_liste

    recursiveGlouton(candidate_list, final_list)


# Allows different criteria for glouton
def relationshipCriteria(x, item):
    return (x.getId() in item.getKnownList())


def potentialScoreCriteria(x, item, candidate_list):
    # Get number of people known among those still possible
    nbRelationships = len(
        list(filter(relationshipCriteria(x, item), candidate_list)))  ## TODO: Refactor to allow better behavior
    return item.weight * nbRelationships
