# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from Convive import Convive


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 2:
        source_file = open(sys.argv[1], "r")
        destination_file = open(sys.argv[2], "w")

        source_data = source_file.readline()
        source_data = source_data.split()

        print(source_data)
        binaries_list = []
        convive_list = []
        destination_file.write("Maximize" + '\n')
        z_max = "z: "

        for i in range(int(source_data[0])):
            coeff_i = source_file.readline().strip().split()

            z_max = z_max + coeff_i[1] + " x" + coeff_i[0] + " + "

            binaries_list.append("x" + coeff_i[0])
            convive_list.append(Convive("x" + coeff_i[0]))
        print(binaries_list)

        for i in range(len(convive_list)):
            convive_list[i].setlisteNonConnu(binaries_list)
        print(binaries_list)

        z_max = z_max[:-2]
        print(z_max)

        destination_file.write(z_max + '\n')
        destination_file.write("Subject To" + '\n')
        for i in range(int(source_data[1])):    #Construction des liens entre les convives ne se connaissant pas
            lien_i_j = source_file.readline().strip().split()

            lien_i_j[0] = "x" + lien_i_j[0]
            lien_i_j[1] = "x" + lien_i_j[1]
            for j in range(len(convive_list)):
                if lien_i_j[0] == convive_list[j].getId():
                    convive_list[j].removeFromList(lien_i_j[1])
                if lien_i_j[1] == convive_list[j].getId():
                    convive_list[j].removeFromList(lien_i_j[0])

        print(convive_list[0].constructPoids())

        for i in range(len(convive_list)):
            destination_file.write(convive_list[i].constructPoids() + '\n')

        destination_file.write("binaries \n")

        for i in range(len(convive_list)):
            destination_file.write(convive_list[i].getId() + '\n')


        destination_file.write("End")
        source_file.close()
        destination_file.close()
    else:
        print("Utilisation : python main.py source.txt destination.lb")


#liste_finale = liste d'ID
#liste_candidate = liste de Convives

##Critère basé sur le nombre de relations pour tenter de maximiser le score. Mais pas le score directement

def recursiveGlouton(liste_candidate, liste_finale):
    # Compter nb personnes connues
    max_so_far = 0
    next_candidate = -1
    #Future liste candidate
    tmp_liste = []
    #Permet de savoir si tous se connaissent
    checkLen = ()

    for item in liste_candidate:

        tmp = list(filter(lambda x: x.getId() in item.getListeConnu(), liste_candidate))
        checkLen.add(len(tmp))
#Algo pour garder le meilleur candidat ( Nb de relations connues)
        if max_so_far < len(tmp):
            tmp_liste = tmp
            max_so_far = len(tmp)
            next_candidate = item.getId()

#Renvoie la liste d'ID des Convives
    if(len(checkLen) == 1):
        return liste_finale


    liste_finale.add(next_candidate)
    liste_candidate = tmp_liste

    recursiveGlouton(liste_candidate, liste_finale)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
