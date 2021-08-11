

# Required dependencies to be installed 
# pip install PyPDF2
# pip install pyttsx3


import PyPDF2

# isko random file path bana loo look at pdf to image conversion bbox visualization
pdfReader = PyPDF2.PdfFileReader(open("file.pdf", "rb"))


import pyttsx3
speaker = pyttsx3.init()


for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()


speaker.save_to_file(text, "audio.mp3")
speaker.runAndWait()

