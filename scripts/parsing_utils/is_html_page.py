def is_html_page(content):
    string_content = str(content)
    if "</head>" in string_content:
        return True
    if "</body>" in string_content:
        return True
    return False
