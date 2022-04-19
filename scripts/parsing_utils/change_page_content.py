from scripts.parsing_utils.calc_len_of_elem import calc_len_of_elem
from scripts.parsing_utils.links_replace import links_replace
from scripts.parsing_utils.modify_classes import modify_classes
from scripts.store_const.get_prohib_chars import get_prohib_chars


def change_page_content(
        page_content,
        string_for_adding_to_words,
        global_url_address,
        global_port):
    page_content = page_content.decode("utf-8")

    page_content = page_content.replace('\t', ' ')
    page_content = page_content.replace('\n', ' ')

    filtered_classes_array = modify_classes(page_content)

    arrows_together = '><'
    arrows_with_separator = '> ' + '$$$%%%@@@%%%$$$' + ' <'

    page_content = page_content.replace(arrows_together, arrows_with_separator)

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

    changed_content_string = changed_content_string.replace(
        arrows_with_separator, arrows_together)
    changed_content_string = changed_content_string.replace(
        '$$$%%%@@@%%%$$$', ' ')

    for name_class in filtered_classes_array:
        with_tm = name_class + string_for_adding_to_words
        changed_content_string = changed_content_string.replace(
            with_tm, name_class)

    return links_replace(
        changed_content_string,
        global_url_address,
        global_port)
