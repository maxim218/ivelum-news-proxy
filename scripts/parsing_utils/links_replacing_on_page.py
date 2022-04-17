def links_replacing_on_page(content):
    content = content.replace('href="http', 'href="#')
    content = content.replace("href='http", "href='#")
    return content
