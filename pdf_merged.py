import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()
print("The 2 files needs to be at the same foldet than this script")
newFileName = input("Enter a name for the final pdf: ")
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write(newFileName + ".pdf")
