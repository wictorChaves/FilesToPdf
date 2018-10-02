import sys
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from ConvertTreeFilesToPdf import ConvertTreeFilesToPdf

messagebox.showinfo("Source folder", "Select the source folder")
input_path = askdirectory()
messagebox.showinfo("Source destiny", "Select the destiny folder")
outputh_path = askdirectory()

convertTreeFilesToPdf = ConvertTreeFilesToPdf(input_path, outputh_path)
convertTreeFilesToPdf.setAllowExtensions(["txt", "php", "js", "html", "htm", "json"])

if not convertTreeFilesToPdf.verifyPaths():
    messagebox.showerror("Error", "Invalid folder!")
    sys.exit(0)

convertTreeFilesToPdf.execute()
