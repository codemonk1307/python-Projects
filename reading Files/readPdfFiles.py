

from PyPDF2 import PdfFileReader

file = open("file.pdf", "rb")
content = PdfFileReader(file)
text = content.getPage(0)
text.extractText()

print(content.numPages)

