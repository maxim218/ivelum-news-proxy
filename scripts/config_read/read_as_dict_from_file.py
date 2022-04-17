def read_as_dict_from_file(name_of_file):
    dict = {}
    f = open(name_of_file, 'r')
    for line in f:
        pair_arr = line.strip().split("=")
        key = pair_arr[0].strip()
        value = pair_arr[1].strip()
        dict[key] = value
    f.close()
    return dict
