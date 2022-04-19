from flask import Flask, request, make_response
from waitress import serve


from scripts.parsing_utils.is_html_page import is_html_page
from scripts.parsing_utils.url_params_string import url_params_string
from scripts.logging_info.print_server_params import print_server_params
from scripts.logging_info.print_logs import print_logs
from scripts.network_http.send_query_to_server import send_query_to_server
from scripts.config_read.read_as_dict_from_file import read_as_dict_from_file
from scripts.headers_utils.create_headers_dict import create_headers_dict
from scripts.parsing_utils.change_page_content import change_page_content


global_url_address = ""
global_verbose = ""
global_port = 0

app = Flask(__name__)


def create_response_obj(answer_from_server_data, headers_array, code):
    resp = make_response(answer_from_server_data, int(code))
    resp.headers = create_headers_dict(headers_array)
    return resp


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all_queries(path):
    global global_url_address
    global global_verbose
    global global_port

    request_args_dict = request.args.to_dict()
    url_pars_str = url_params_string(request_args_dict)
    full_url_address = global_url_address + path + url_pars_str
    (page_content, headers, code) = send_query_to_server(full_url_address)
    is_html_flag = is_html_page(page_content)

    if 'yes' == global_verbose:
        print_logs(full_url_address, is_html_flag)

    if not is_html_flag:
        return create_response_obj(page_content, headers, code)
    else:
        modified_page_content = change_page_content(
            page_content, '™', global_url_address, global_port)
        return create_response_obj(modified_page_content, headers, code)


if __name__ == '__main__':
    config_dict = read_as_dict_from_file("config.txt")
    global_url_address = config_dict['url']
    global_verbose = config_dict['verbose']
    port = config_dict['port']
    global_port = config_dict['port']
    print_server_params(global_url_address, global_verbose, port)
    serve(app, host="0.0.0.0", port=int(port))
