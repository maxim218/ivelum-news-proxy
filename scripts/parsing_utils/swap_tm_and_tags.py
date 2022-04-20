from scripts.store_const.get_repeat_depth import get_repeat_depth


def swap_tm_and_tags(tm_string, tags_list, page_content):
    depth = get_repeat_depth()

    for i in range(0, depth):
        for tag_element in tags_list:
            tag = str(tag_element)
            full_tag_data = '<' + tag + '>'
            page_content = page_content.replace(
                full_tag_data + tm_string, tm_string + full_tag_data)
            full_tag_data = '<' + '/' + tag + '>'
            page_content = page_content.replace(
                full_tag_data + tm_string, tm_string + full_tag_data)

    return page_content
