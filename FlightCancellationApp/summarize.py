import PyPDF2
import os

def pdf_to_text(pdf_path):
    text=''
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader=PyPDF2.PdfReader(pdf_file)

            for page_num in range(len(pdf_reader.pages)):
                page=pdf_reader.pages[page_num]
                text+=page.extract_text()

    return text