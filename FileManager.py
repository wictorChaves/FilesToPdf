import os

def makeDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
