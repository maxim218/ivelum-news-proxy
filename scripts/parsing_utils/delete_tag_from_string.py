from scripts.parsing_utils.has_not_opened_tag import has_not_opened_tag


def delete_tag_from_string(string_with_tag):
    if has_not_opened_tag(string_with_tag):
        string_with_tag = '<' + string_with_tag
    buf_string = ""
    flag_add = True
    length = len(string_with_tag)
    for i in range(0, length):
        current_char = string_with_tag[i]
        if '<' == current_char:
            flag_add = False
            continue
        if '>' == current_char:
            flag_add = True
            continue
        if flag_add:
            buf_string += current_char
    return buf_string
