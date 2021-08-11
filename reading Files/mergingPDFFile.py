

# pip install PyPDF2
# python script to merge 2 pdf into 1
from PyPDF2 import PdfFileReader, PdfFileMerger

# take both files as input and read them
file1 = PdfFileReader("file1.pdf")
file2 = PdfFileReader("file2.pdf")

# create a pdf file merger object
output = PdfFileMerger()

# append both the pdf reader object into it 
output.append(file1)
output.append(file2)

# saving the merged pdf 
output.write("mergedFile.pdf")

