import os
from os import walk
from ConvertTextToPdf import textToPdf

def makeDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

input_path = 'E:\\Wictor\\Workspace\\Python\\FilesToPdf\\Input'
outputh_path = 'E:\\Wictor\\Workspace\\Python\\FilesToPdf\\Output'
allow_extensions = ["txt", "php", "js"]

for (dirpath, dirnames, filenames) in walk(input_path):

    new_dir = dirpath.replace(input_path, outputh_path) + "\\"
    old_dir = dirpath + "\\"

    makeDir(new_dir)

    for file in filenames:
        extension = file.split('.')[-1]
        if extension.lower() in allow_extensions:
            new_file = new_dir + file + ".pdf"
            old_file = old_dir + file
            textToPdf(old_file, new_file)


