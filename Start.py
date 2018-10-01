import sys
from os import walk
from FileManager import makeDir
from ConvertTextToPdf import textToPdf
from tkinter.filedialog import askdirectory

input_path = askdirectory()
outputh_path = askdirectory()

if type(input_path) != str or type(outputh_path) != str or input_path == '' or outputh_path == '':
    print("Pasta inválida!")
    sys.exit(0)

#input_path = 'E:\\Wictor\\Workspace\\Python\\FilesToPdf\\Input'
#outputh_path = 'E:\\Wictor\\Workspace\\Python\\FilesToPdf\\Output'

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


