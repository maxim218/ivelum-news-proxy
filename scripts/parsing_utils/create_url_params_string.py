def create_url_params_string(request_args_dict):
    url_params_string = "?"
    for key, value in request_args_dict.items():
        pair_string = key + "=" + value + "&"
        url_params_string += pair_string
    return url_params_string[:len(url_params_string) - 1]
