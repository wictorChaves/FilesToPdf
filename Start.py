import sys
from tkinter import messagebox
from ConfigFile import allow_extensions
from tkinter.filedialog import askdirectory
from ConvertTreeFilesToPdf import ConvertTreeFilesToPdf

messagebox.showinfo("Source folder", "Select the source folder")
input_path = askdirectory()
messagebox.showinfo("Source destiny", "Select the destiny folder")
outputh_path = askdirectory()

convertTreeFilesToPdf = ConvertTreeFilesToPdf(input_path, outputh_path)
convertTreeFilesToPdf.setAllowExtensions(allow_extensions)

if not convertTreeFilesToPdf.verifyPaths():
    messagebox.showerror("Error", "Invalid folder!")
    sys.exit(0)
try:
    convertTreeFilesToPdf.execute()
    messagebox.showinfo("Finisher", "Process completed")
except Exception as e:
    messagebox.showerror("Error", str(e))
    print(str(e))
    sys.exit(0)



