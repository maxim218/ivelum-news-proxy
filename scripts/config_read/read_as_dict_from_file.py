from scripts.config_read.line_parse import line_parse


def read_as_dict_from_file(name_of_file):
    dict_config = {}
    f = open(name_of_file, 'r')
    for line in f:
        line_parse(dict_config, line)
    f.close()
    return dict_config
