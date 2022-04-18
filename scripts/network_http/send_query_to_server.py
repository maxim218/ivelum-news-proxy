import urllib.request


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
