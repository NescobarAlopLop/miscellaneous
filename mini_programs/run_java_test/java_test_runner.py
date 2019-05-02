import os
import sys
from typing import List, Tuple
import re
import csv
import zipfile


def get_file_names_and_paths(main_dir: str = ".") -> List[Tuple[str,str]]:
    rv = []
    for root, directories, filenames in os.walk(main_dir):
        for filename in filenames:
            if filename.endswith('zip'):
                rv.append((os.path.join(root, filename), root))
            else:
                print('not a zip file: {}'.format(filename))
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
    with open(file_path_name, 'w', newline='\n') as myfile:
        wr = csv.writer(myfile)
        for val in in_list:
            wr.writerow([val])


if __name__ == '__main__':

    files_paths = get_file_names_and_paths("/home/ge/Documents/miscellaneous/mini_programs/run_java_test/test_files/Lab2")
    print(files_paths)
    # /usr/lib/jvm/java-12-oracle/bin/java -jar FindPrimeNumbers.jar 200 20 5
    # path = "."
    # if len(sys.argv) > 1:
    #     path = sys.argv[1]
    # ids = get_unique_ids_from_folder(path)
    # print(ids)
    # print(len(ids))
    # save_list_as_csv(ids, path + "ids.csv")
