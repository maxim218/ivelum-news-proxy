def links_replace(content, global_url_address, global_port):
    localhost_address = " " + "http://localhost:" + str(global_port)

    content = content.replace(global_url_address, localhost_address)
    global_url_address = global_url_address[:len(global_url_address) - 1]
    content = content.replace(global_url_address, localhost_address)

    content = content.replace('href="http', 'href="#')
    content = content.replace("href='http", "href='#")

    return content
