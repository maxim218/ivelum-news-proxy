import os
from os import listdir
from os.path import isfile, join
import pathlib


def is_file_python_code(path):
    type_string = ".py"
    is_python = path.endswith(type_string)
    return is_python


def get_files_list(path, arr):
    for element in listdir(path):
        new_path = join(path, element)
        if isfile(new_path):
            is_python = is_file_python_code(new_path)
            if is_python:
                arr.append(new_path)
        else:
            get_files_list(new_path, arr)


def print_python_files_names(arr):
    count = 0
    for element in arr:
        count = count + 1
        print(str(count) + ") " + element)


def fix_simple_errors(arr):
    for element in arr:
        os.system("autopep8 --select=W293 --in-place " + element)
        os.system("autopep8 -aaa -d " + element)
        os.system("autopep8 -aaa -i " + element)


def run_pycodestyle_code_control(arr):
    line_string = "-------------------------"
    for element in arr:
        print(line_string)
        print("File path: " + element)
        os.system("pycodestyle " + element)


mass = []
current_path = pathlib.Path().resolve()
get_files_list(current_path, mass)
print_python_files_names(mass)
fix_simple_errors(mass)
run_pycodestyle_code_control(mass)
