import os
from pathlib import Path

def makeDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def fileExist(path):
    my_file = Path(path)
    if my_file.is_file():
        return True
    return False
