from scripts.parsing_utils.calc_len_of_elem import calc_len_of_elem
from scripts.parsing_utils.links_replace import links_replace
from scripts.store_const.get_prohib_chars import get_prohib_chars


def change_page_content(page_content, string_for_adding_to_words):
    page_content = page_content.decode("utf-8")

    page_content = page_content.replace('\t', ' ')
    page_content = page_content.replace('\n', ' ')
    page_content = page_content.replace('<', ' <')
    page_content = page_content.replace('>', '> ')
    page_content = str(page_content)

    arr = page_content.split(' ')
    length = len(arr)

    for i in range(0, length):
        element = arr[i]
        if 6 == calc_len_of_elem(element):
            element += string_for_adding_to_words
        arr[i] = element

    changed_content_string = ' '.join(arr)

    special_chars_arr = get_prohib_chars()
    for i in range(0, len(special_chars_arr)):
        char_element = special_chars_arr[i]
        old_val = char_element + string_for_adding_to_words
        new_val = string_for_adding_to_words + char_element
        changed_content_string = changed_content_string.replace(
            old_val, new_val)

    return links_replace(changed_content_string)
