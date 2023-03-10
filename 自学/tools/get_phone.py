
import os

import pytest
import yaml

dir_path = os.getcwd()
def get_phone():
    for file in os.listdir(dir_path):
        if file.endswith(".yml"):
            file_path = os.path.join(dir_path, file)
            with open(file_path, "r") as f:
                data = yaml.safe_load(f)
                return data

if __name__ == '__main__':
    a = get_phone()
    print(a)