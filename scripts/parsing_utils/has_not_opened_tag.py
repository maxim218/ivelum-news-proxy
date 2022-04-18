def has_not_opened_tag(string_with_tag):
    length = len(string_with_tag)
    for i in range(0, length):
        current_char = string_with_tag[i]
        if '<' == current_char:
            return False
        if '>' == current_char:
            return True
    return False
