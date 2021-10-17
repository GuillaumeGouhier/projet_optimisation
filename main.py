import sys
from Guest import Guest
from LpConstructor import openFilesAndCreateLPFile
from func import init_list
from functions import initPop, nextGeneration
from Solution import Solution


# final_list = liste d'ID
# candidate_list = liste de Convives

##Critère basé sur le nombre de relations pour tenter de maximiser le score. Mais pas le score directement

def recursiveGlouton(candidate_list, final_list):
    # Compter nb personnes connues
    max_so_far = 0
    next_candidate = -1
    # Future liste candidate
    tmp_liste = []
    # Permet de savoir si tous se connaissent
    checkLen = set()

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

        final_list.extend(list(map(lambda x: x.getId(), candidate_list)))
        ## Translate list of ids to genes
        print("Liste finale: ", final_list)
        genes = [0 for i in range(len(guest_list))]
        for i in final_list:
            genes[int(i)] = 1
        print("Genes Glouton: ", genes)

        ## Construct Solution object
        result = Solution(genes)
        return result

    final_list.append(next_candidate)
    candidate_list = tmp_liste

    return recursiveGlouton(candidate_list, final_list)


# Allows different criteria for glouton
def relationshipCriteria(x, item):
    return (x.getId() in item.getKnownList())


def potentialScoreCriteria(x, item, candidate_list):
    # Get number of people known among those still possible
    nbRelationships = len(
        list(filter(relationshipCriteria(x, item), candidate_list)))  ## TODO: Refactor to allow better behavior
    return item.weight * nbRelationships


## Main

if __name__ == '__main__':
    if len(sys.argv) > 2:
        binaries_list = []
        guest_list = []

        ## Generation LP file
        # openFilesAndCreateLPFile(sys.argv[1], sys.argv[2], binaries_list, guest_list)

        ## Re init data
        guest_list = init_list(sys.argv[1])

        # Generate first glouton solution
        NIL_Guests = []
        local_solution = recursiveGlouton(guest_list, NIL_Guests)

        # Perform Genetic Algorithm
        population = initPop(100, guest_list)
        while (True):
            population = nextGeneration(population)
            print(len(population))

        # Perform other metaheuristics



    else:
        print("Utilisation : python main.py source.txt destination.lp")
