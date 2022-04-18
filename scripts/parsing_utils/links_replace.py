def links_replace(content):
    content = content.replace('href="http', 'href="#')
    content = content.replace("href='http", "href='#")
    return content
