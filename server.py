from flask import Flask, request, make_response
from waitress import serve
import urllib.request

global_url_address = ""
global_verbose = ""

app = Flask(__name__)

def is_header_allowed(header):
    prohibited_headers = ["CONNECTION", "CONTENT-LENGTH", "TRANSFER-ENCODING"]
    header_in_array_flag = (header.upper() in prohibited_headers)
    return (header_in_array_flag == False)

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


def create_response_obj(answer_from_server_data, headers_array):
    resp = make_response(answer_from_server_data)
    resp.headers = create_headers_dict(headers_array)
    return resp

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

def create_url_params_string(request_args_dict):
    url_params_string = "?"
    for key, value in request_args_dict.items():
        pair_string = key + "=" + value + "&"
        url_params_string += pair_string
    return url_params_string[:len(url_params_string) - 1]

def is_html_page(content):
    string_content = str(content)
    if "</head>" in string_content: 
        return True
    if "</body>" in string_content: 
        return True
    return False


def has_string_not_opened_tag(string_with_tag):
    length = len(string_with_tag)
    for i in range(0, length):
        current_char = string_with_tag[i]
        if('<' == current_char):
            return False
        if('>' == current_char):
            return True
    return False

def delete_tag_from_string(string_with_tag):
    if(has_string_not_opened_tag(string_with_tag)):
        string_with_tag = '<' + string_with_tag
    buf_string = ""
    flag_add = True
    length = len(string_with_tag)
    for i in range(0, length):
        current_char = string_with_tag[i]
        if('<' == current_char):
            flag_add = False 
            continue
        if('>' == current_char):
            flag_add = True
            continue
        if(flag_add):
            buf_string += current_char
    return buf_string
    

def calc_len_of_page_element(string_element):
    buf_string = str(string_element)

    chars_prohibited = [' ', ',', '.', '"', '\t', '\n', "'"]
    for i in range(0, len(chars_prohibited)):  
        current = chars_prohibited[i]
        buf_string = "".join(buf_string.split(current)) 

    buf_string = delete_tag_from_string(buf_string)

    length = len(buf_string)
    return length


def change_page_content(page_content, string_for_adding_to_words):
    page_content = page_content.decode("utf-8")

    page_content = page_content.replace('\t', ' ')
    page_content = page_content.replace('\n', ' ')
    page_content = page_content.replace('\n', ' ')

    page_content = page_content.replace('<', ' <')
    page_content = page_content.replace('>', '> ')

    page_content = str(page_content)

    arr = page_content.split(' ')
    length = len(arr)
    for i in range(0, length):
        element = arr[i]
        if(6 == calc_len_of_page_element(element)):
            element += string_for_adding_to_words
        arr[i] = element 
    changed_content_string = ' '.join(arr)
    return changed_content_string

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all_queries(path):
    global global_url_address
    global global_verbose
    request_args_dict = request.args.to_dict()
    url_params_string = create_url_params_string(request_args_dict)
    full_url_address = global_url_address + path + url_params_string
    (page_content, headers) = send_query_to_server(full_url_address)
    is_html_flag = is_html_page(page_content)
    if('yes' == global_verbose):
        print("Full url address: " + full_url_address + "  Html: " + str(is_html_flag))
    if(False == is_html_flag):
        return create_response_obj(page_content, headers)
    else:
        modified_page_content = change_page_content(page_content, '™')
        return create_response_obj(modified_page_content, headers)

def print_server_params(url, verbose, port):
    print('\n')
    print("Url address: " + url)
    print("Verbose rendering: " + verbose)
    print("Port number: " + port)
    print('\n')

def send_query_to_server(url):
    try:
        url = str(url)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        content = response.read()
        headers = response.getheaders()
        return (content, headers)
    except Exception:
        content = "<h1>Can not open resource</h1>"
        return (content, None)

if __name__ == '__main__':
    config_dict = read_as_dict_from_file("config.txt")
    global_url_address = config_dict['url']
    global_verbose = config_dict['verbose']
    port = config_dict['port']
    print_server_params(global_url_address, global_verbose, port)
    serve(app, host="0.0.0.0", port=int(port))
