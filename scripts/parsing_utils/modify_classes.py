from scripts.parsing_utils.is_class_string import is_class_string


def modify_classes(page_content):
    arr = list(page_content)
    length = len(arr)

    classes_names_string = " "
    adding_flag = False

    i = 0
    while i < length:
        if is_class_string(i, arr):
            i = i + 7
            adding_flag = True
            continue
        if '"' == arr[i]:
            adding_flag = False
            classes_names_string += ' '
        if adding_flag:
            classes_names_string += arr[i]
        i = i + 1

    while classes_names_string.find("  ") > -1:
        classes_names_string = classes_names_string.replace("  ", " ")
        classes_names_string = classes_names_string.strip()

    classes_array = classes_names_string.strip().split(' ')
    classes_set = set(classes_array)
    classes_array = list(classes_set)

    filtered_classes_array = filter(
        lambda element: len(element) == 6, classes_array)
    filtered_classes_array = list(filtered_classes_array)

    return filtered_classes_array
