import os
import sys
from typing import List, Tuple
import re
import csv
import zipfile


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
    files_paths = get_file_names_and_paths("/home/ge/Documents/miscellaneous/mini_programs/run_java_test/test_files/Lab2")
    arguments = '200 20 5'

    for file_path_tup in files_paths:
        file_name = file_path_tup[0]
        dir_path = file_path_tup[1]
        if file_name.endswith('zip'):
            unzip_file(file_name, dir_path)
        command = '{} {} {}'.format(command_to_run, file_path_tup[0], arguments)

    file_name = 'FindPrimeNumbers.jar'

    if file_name.endswith('zip'):
        pass
    print(files_paths)

    # ids = get_unique_ids_from_folder(path)
    # print(ids)
    # print(len(ids))
    # save_list_as_csv(ids, path + "ids.csv")
