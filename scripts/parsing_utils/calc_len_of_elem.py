from scripts.parsing_utils.delete_tag_from_string import delete_tag_from_string
from scripts.store_const.get_prohib_chars import get_prohib_chars


def calc_len_of_elem(string_element):
    buf_string = str(string_element)

    chars_prohibited = get_prohib_chars()
    for i in range(0, len(chars_prohibited)):
        current = chars_prohibited[i]
        buf_string = "".join(buf_string.split(current))

    buf_string = delete_tag_from_string(buf_string)

    length = len(buf_string)
    return length
