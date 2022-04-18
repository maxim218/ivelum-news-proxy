from scripts.headers_utils.is_header_allowed import is_header_allowed


def create_headers_dict(headers_arr):
    if(headers_arr is None):
        return {}
    dict = {}
    length = len(headers_arr)
    for i in range(0, length):
        (key, value) = headers_arr[i]
        if(is_header_allowed(key)):
            dict[key] = value
    return dict
