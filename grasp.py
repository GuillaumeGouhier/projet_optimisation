import random


def GRASP(candidate_list, final_list):
    print("\n Candidate list: ", candidate_list)
    print("\n Final list: ", final_list)
    # Compter nb personnes connues
    max_so_far = 0
    next_candidate = -1
    # Future liste candidate
    tmp_liste = []
    # Permet de savoir si tous se connaissent
    checkLen = ()

    #############################""
    # liste des potentiels meilleur guest
    list_rd = []

    ################################

    for item in candidate_list:

        tmp = list(filter(lambda x: x.getId() in item.getKnownList(), candidate_list))
        checkLen.add(len(tmp))
        # Algo pour garder le meilleur candidat ( Nb de relations connues)
        if max_so_far < len(tmp):
            tmp_liste = tmp
            max_so_far = len(tmp)
            next_candidate = item.getId()
            #########################
            # ajoue des 5 meilleurs personnes
            list_rd.append(next_candidate)  # on met tout les personnes qui se son batue pour ètres la personne qui connais le plus de monde

        if len(list_rd) > 5:  # si il en a plus de 5 alors on prend les 5 dernière pk c'est les meilleur
            list_rd = list_rd[-5:]
        # si y en a moin qui se sont batuent pas de soucie
        next_candidate = choix_rd(list_rd)  # on prend une des 5 personnes au hazard

        ##################""

    # Renvoie la liste d'ID des Convives
    if (len(checkLen) == 1):
        return final_list

    final_list.add(next_candidate)
    candidate_list = tmp_liste

    GRASP(candidate_list, final_list)


#ON choisi 1 convive parmie la liste
def choix_rd(list_rd):
  return random.choice(list_rd)