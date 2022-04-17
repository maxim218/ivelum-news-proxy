from scripts.parsing_utils.calc_len_of_page_element import calc_len_of_page_element
from scripts.parsing_utils.links_replacing_on_page import links_replacing_on_page

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
        if(6 == calc_len_of_page_element(element)):
            element += string_for_adding_to_words
        arr[i] = element 
    
    changed_content_string = ' '.join(arr)

    special_chars_arr = [' ', ',', '.', '"', "'", '?', '!', ';']
    for i in range(0, len(special_chars_arr)):
        char_element = special_chars_arr[i]
        old_val = char_element + string_for_adding_to_words
        new_val = string_for_adding_to_words + char_element
        changed_content_string = changed_content_string.replace(old_val, new_val)

    return links_replacing_on_page(changed_content_string)
