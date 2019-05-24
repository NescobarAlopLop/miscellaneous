import os
import sys
from typing import List, Tuple, Optional
import re
import csv
import zipfile
import shutil
import subprocess


def get_file_names_and_paths(main_dir: str = ".") -> List[Tuple[str, str]]:
    rv = []
    for root, directories, filenames in os.walk(main_dir):
        for filename in filenames:
            rv.append((os.path.join(root, filename), root))
    return rv


def unzip_file(path_to_zip_file: str, directory_to_extract_to: str):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()


def get_test_file(main_dir, extention='jar'):
    for root, directories, filenames in os.walk(main_dir):
        for filename in filenames:
            if filename.endswith(extention):
                return os.path.join(root, filename)


def get_unique_ids_from_folder(folder_path: str = '.') -> List[int]:
    rv = set()
    for _, _, filenames in os.walk(folder_path):
        for filename in filenames:
            ids = re.findall(r"\d+", filename)
            for i_d in ids:
                rv.add(int(i_d))
    return sorted(list(rv))


def save_list_as_csv(in_list: List, file_path_name: str):
    with open(file_path_name, 'w', newline='\n') as w_file:
        wr = csv.writer(w_file)
        for val in in_list:
            wr.writerow([val])


def get_student_ids_from_string(s: str):
    return re.findall(r"\d+", s)


if __name__ == '__main__':
    # print("HOW TO:")
    # print("follow the script file name with:\n\t "
    #       "- path to lab folder\n\t "
    #       "- command to run\n\t "
    #       "- arguments to runnable file\n"
    #       "Example: python3 java_test_runner.py /home/ge/labs/Lab2/ java -jar")

    path = "."
    command_to_run = '/usr/lib/jvm/java-12-oracle/bin/java -jar'

    if len(sys.argv) > 1:
        path = sys.argv[1]
    # if len(sys.argv) > 2:
    #     command_to_run = sys.argv[2]
    lab_path = "/home/ge/Documents/miscellaneous/mini_programs/run_java_test/test_files/Lab2"
    files_paths = get_file_names_and_paths(lab_path)
    arguments = '200 20 5'

    for file_path_tup in files_paths:
        file_name = file_path_tup[0]
        dir_path = file_path_tup[1]
        if file_name.endswith('zip'):
            students_ids_str = file_name.split('/')[-1].split('.')[0] + '.jar'
            # print("students: {}".format(get_student_ids_from_string(students_ids_str)))
            unzip_file(file_name, dir_path)
            file_to_test = get_test_file(dir_path, extention='jar')
            if file_to_test is None:
                print("jar doesnt exist\n\t{}".format(dir_path))
                continue
            new_test_file_path = os.path.join(lab_path, students_ids_str)
            # print(file_to_test)
            # print(new_test_file_path)
            try:
                shutil.copy(file_to_test, new_test_file_path)
            except shutil.SameFileError:
                pass
            command = '{} \'{}\' {}'.format(command_to_run, new_test_file_path, arguments)
            print(command)
            subprocess.call(command)

    print(len(files_paths))
    file_name = 'FindPrimeNumbers.jar'

    if file_name.endswith('zip'):
        pass
    # print(files_paths)

    # ids = get_unique_ids_from_folder(path)
    # print(ids)
    # print(len(ids))
    # save_list_as_csv(ids, path + "ids.csv")
