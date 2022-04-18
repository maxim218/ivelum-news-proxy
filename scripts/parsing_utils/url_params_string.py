def url_params_string(request_args_dict):
    url_pars_string = "?"
    for key, value in request_args_dict.items():
        pair_string = key + "=" + value + "&"
        url_pars_string += pair_string
    return url_pars_string[:len(url_pars_string) - 1]
