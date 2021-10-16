def init_data(source):
    # Initialize guest_list with data in it
    guest_list = init_list()


def init_list(fp):
    # Read data source
    data = []
    data = parsefile(fp)
    return data



def parsefile(fp):

    result = []

    fd = open(fp, 'r')
    file_data = fd.readLine().split()

    for i in range(int(file_data[0])):
        coeff_i = fd.readline().strip().split()
        result.append(Guest("x" + coeff_i[0]))

        # Construct Known List
    return result

def constructKnownList(data, fd):


    for i in range(int(source_data[0]), int(source_data[1])):  # Construction des liens entre les convives ne se connaissant pas
        lien_i_j = fd.readline().strip().split()

        lien_i_j[0] = "x" + lien_i_j[0]
        lien_i_j[1] = "x" + lien_i_j[1]
        for j in range(len(guest_list)):
            if lien_i_j[0] == guest_list[j].getId():
                guest_list[j].addtoKnownList(lien_i_j[1])
            if lien_i_j[1] == guest_list[j].getId():
                guest_list[j].addtoKnownList(lien_i_j[0])
    # Add known people to every guest

    # Based on LP construction but extended

    return data