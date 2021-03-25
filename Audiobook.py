# pyttsx3 -> python text-to-speech module
import pyttsx3
import PyPDF2

class Pdf :
    def open_book(self):
        global pdfReader
     # opening the book
     # here rb means reading as a binary book
        book=open(self, "rb")
     # reading book
        pdfReader=PyPDF2.PdfFileReader(book)
     # printing pages
        pages=pdfReader.numPages
        print("This book have {} pages".format(pages))

    def speakerInitialize(self):
        global speaker
     # initialize the speaker variable
        speaker=pyttsx3.init()
     # setting to female voice
        voices=speaker.getProperty('voices')
        speaker.setProperty('voice', voices[1].id)
     # letting speaker say something
        speaker.say("Hello Dear User ! Today we will read {}". format(self))

file = input("Enter name of pdf : ")
Pdf.open_book(file);
begin_page = int(input("Enter starting page from where you want to listen : "))
end_page = int(input("Enter ending page from where you want to listen : "))
Pdf.speakerInitialize(file)
for num in range(begin_page, end_page+1):
        text=pdfReader.getPage(num).extractText()
        speaker.say(text)
        # making speaker run and wait
        speaker.runAndWait()
print("Thank you !!")