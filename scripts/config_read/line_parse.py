def line_parse(dict_config, line):
    if len(line) > 3:
        pair_arr = line.strip().split("=")
        key = pair_arr[0].strip()
        value = pair_arr[1].strip()
        dict_config[key] = value
    else:
        pass
