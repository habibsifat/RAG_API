import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
        return text

def append_text_to_file(text, file_path):
    with open(file_path, 'a') as file:
        file.write("\n" + text)

pdf_path = '/Users/kibtia/Downloads/RAG_API/pdf/1.pdf'
new_data_file_path = '/Users/kibtia/Downloads/RAG_API/new_data.txt'

pdf_text = extract_text_from_pdf(pdf_path)
append_text_to_file(pdf_text, new_data_file_path)

print("PDF text has been appended to new_data.txt")