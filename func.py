def init_data(source):
    # Initialize guest_list with data in it
    guest_list = init_list()


def init_list():
    # Read data source
    data = []

    return data



def parsefile(fp):
    fd = open(fp, 'r')
    file_data = fd.readLine().split()

    for i in range(int(file_data[0])):
        coeff_i = fd.readline().strip().split()