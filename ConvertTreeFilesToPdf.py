from os import walk
from FileManager import makeDir
from ConvertTextToPdf import textToPdf

class ConvertTreeFilesToPdf:

    input_path = ''
    outputh_path = ''
    allow_extensions = []

    def __init__(self, input_path, outputh_path):
        self.input_path = input_path
        self.outputh_path = outputh_path

    def setAllowExtensions(self, extensions):
        self.allow_extensions = extensions

    def verifyPaths(self):
        if type(self.input_path) != str or type(self.outputh_path) != str:
            return False
        if self.input_path == '' or self.outputh_path == '':
            return False
        return True

    def execute(self):

        if not self.verifyPaths():
            print("Invalid folder!")
            return False

        for (dirpath, dirnames, filenames) in walk(self.input_path):

            new_dir = dirpath.replace(self.input_path, self.outputh_path) + "\\"
            old_dir = dirpath + "\\"

            makeDir(new_dir)

            for file in filenames:
                extension = file.split('.')[-1]
                if extension.lower() in self.allow_extensions:
                    new_file = new_dir + file + ".pdf"
                    old_file = old_dir + file
                    textToPdf(old_file, new_file)
