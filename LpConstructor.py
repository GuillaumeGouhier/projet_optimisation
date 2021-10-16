from Guest import Guest
import sys


def openFilesAndCreateLPFile(sfile, dfile, blist, glist):

    source_file = open(sfile, "r")
    destination_file = open(dfile, "w")
    source_data = source_file.readline()
    source_data = source_data.split()

    print(source_data)
    makeMaximisationEquation(source_file, destination_file, source_data, blist, glist)

def makeMaximisationEquation(source_file, destination_file, source_data, binaries_list, guest_list):

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
    createAllContraint(source_file, destination_file, source_data, binaries_list, guest_list)

def createAllContraint(source_file, destination_file, source_data, binaries_list, guest_list):

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

    writeVariableInFile(source_file, destination_file, source_data, binaries_list, guest_list)


def writeVariableInFile(source_file, destination_file, source_data, binaries_list, guest_list):

    destination_file.write("binaries \n")

    for i in range(len(guest_list)):
        destination_file.write(guest_list[i].getId() + '\n')

    destination_file.write("End")
    source_file.close()
    destination_file.close()