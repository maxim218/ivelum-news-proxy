import urllib.request
import requests


def send_query_to_server(url):
    try:
        url = str(url)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        content = response.read()
        headers = response.getheaders()
        return content, headers, response.code
    except Exception:
        r = requests.get(url)
        content = r.text
        return content, None, r.status_code
