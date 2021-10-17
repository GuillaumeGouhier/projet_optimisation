from Guest import Guest

def init_data(source):
    # Initialize guest_list with data in it
    guest_list = init_list(source)
    return guest_list


def init_list(fp):
    # Read data source
    data = []
    data = parsefile(fp)


    return data


def parsefile(fp):
    result = []

    fd = open(fp, 'r')
    file_data = fd.readline().split()

    for i in range(int(file_data[0])):
        coeff_i = fd.readline().strip().split()
        result.append(Guest(coeff_i[0]))

        # Construct Known List
    fd.close()

    tmp = constructKnownList(result, fp)

    return tmp


def constructKnownList(data, fp):

    fd = open(fp, 'r')
    lines = fd.readlines()
    print(lines[0].strip().split()[0])
    for i in range(int(lines[0].strip().split()[0]), int(lines[0].strip().split()[1])):  # Construction des liens entre les convives
        print("coucou")
        lien_i_j = lines[i].strip().split()

        print("Lien :",lien_i_j)
        for j in range(len(data)):
            if lien_i_j[0] == data[j].getId():
                data[j].addtoKnownList(lien_i_j[1])
            if lien_i_j[1] == data[j].getId():
                data[j].addtoKnownList(lien_i_j[0])
    # Add known people to every guest

    # Based on LP construction but extended

    return data
