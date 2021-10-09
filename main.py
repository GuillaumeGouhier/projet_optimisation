# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from Convive import Convive
from Glouton import Glouton

#def filter_nbConnaissance(file):
#    for line in file:
#        if valeur_aFiltré in line:
#            yield line

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

        #print(source_data)
        binaries_list = []
        convive_list = []
        glouton_list = [] #Récupère tous les
        result_choix = Glouton(999,999) # Pour récupérer le convive avec le plus de connaissance
        destination_file.write("Maximize" + '\n')
        z_max = "z: "

        for i in range(int(source_data[0])):
            coeff_i = source_file.readline().strip().split()

            z_max = z_max + coeff_i[1] + " x" + coeff_i[0] + " + "

            binaries_list.append("x" + coeff_i[0])
            #print(Convive("x"+ coeff_i[0]).getId())
            convive_list.append(Convive("x" + coeff_i[0]))
        #print(convive_list)

        for i in range(len(convive_list)):
            convive_list[i].setlisteNonConnu(binaries_list)
        #print(binaries_list)

        z_max = z_max[:-2]
        #print(z_max)

        destination_file.write(z_max + '\n')
        destination_file.write("Subject To" + '\n')
        for i in range(int(source_data[1])):    #Construction des liens entre les convives ne se connaissant pas
            lien_i_j = source_file.readline().strip().split()

            lien_i_j[0] = "x" + lien_i_j[0]
            lien_i_j[1] = "x" + lien_i_j[1]

           # print(lien_i_j[0]+", "+lien_i_j[1])
            for j in range(len(convive_list)):
                if lien_i_j[0] == convive_list[j].getId():
                    convive_list[j].removeFromList(lien_i_j[1])
                if lien_i_j[1] == convive_list[j].getId():
                    convive_list[j].removeFromList(lien_i_j[0])

        #print(convive_list[0].constructPoids())

        for i in range(len(convive_list)):
            destination_file.write(convive_list[i].constructPoids() + '\n')
            glouton_list.append(Glouton(convive_list[i].getId(), convive_list[i].getLenNonConnu()))


        destination_file.write("binaries \n")

        for i in range(len(convive_list)):
            destination_file.write(convive_list[i].getId() + '\n')


        destination_file.write("End")
        source_file.close()
        destination_file.close()
        for i in range(len(glouton_list)): #
            result_choix = glouton_list[i].critere_choix(glouton_list[i].getNbConnaissance(), glouton_list[i].getId(), result_choix.getId(), result_choix.getNbConnaissance())
        print(result_choix.id)
        print(result_choix.nb_connaissance)
    else:
        print("Utilisation : python main.py source.txt destination.lb")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
