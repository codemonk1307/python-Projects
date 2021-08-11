


# Method - 1
import docx2txt

content = doctx2txt.process("file.docx")

print(content)


# Method - 2    VS Code default method
import readDocxFiles

# get the title of the docx file
content = readDocxFiles.__name__
texts = readDocxFiles.__file__
files = readDocxFiles.__package__

print(content)
print(texts)
print(files)

