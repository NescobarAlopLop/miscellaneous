import os
import sys
from typing import List
import re
import csv


def get_unique_ids_from_folder(folder_path: str = '.') -> List[int]:
    rv = set()
    for _, _, filenames in os.walk(folder_path):
        for filename in filenames:
            ids = re.findall(r"\d+", filename)
            for id in ids:
                rv.add(int(id))
    return sorted(list(rv))


def save_list_as_csv(in_list: List, file_path_name: str):
    with open(file_path_name, 'w', newline='\n') as myfile:
        wr = csv.writer(myfile)
        for val in in_list:
            wr.writerow([val])


if __name__ == '__main__':
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]
    ids = get_unique_ids_from_folder(path)
    print(ids)
    print(len(ids))
    save_list_as_csv(ids, path + "ids.csv")
