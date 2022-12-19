# importing packages 
import pyttsx3
import PyPDF2

# opening the pdf
with open('Thebook.pdf','rb') as Book: # rb means Reading Bytes and we are defining it as Book
  reader = PyPDF2.PdfFileReader(Book)
  # the reader that we hear
  audio_reader = pyttsx3.init()
  # setting the speed
  audio_reader.setProperty('rate', 150)

  # getting the pages 
  for page in range(reader.numPages):
    next_page = reader.getPage(page)
    content = next_page.extractText()
  # saying it
    audio_reader.say(content)
    audio_reader.runAndWait()
