def is_class_string(index, arr):
    try:
        class_list_elements = ['c', 'l', 'a', 's', 's', '=', '"']
        logic_and = True
        for character in class_list_elements:
            logic_and = logic_and and (character == arr[index])
            index = index + 1
        return logic_and
    except Exception:
        return False
