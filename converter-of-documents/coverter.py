import fitz  # PyMuPDF
from docx import Document

def pdf_to_text(pdf_path):#this is for pdf convertion
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

def text_to_word(text, output_path):#getting text from pdf
    doc = Document()
    doc.add_paragraph(text)

    doc.save(output_path)

if __name__ == "__main__":
    pdf_path = "resume.pdf"
    output_path = "resume.docx"

    text_content = pdf_to_text(pdf_path)
    text_to_word(text_content, output_path)

    print(f"Conversion complete. Word file saved to {output_path}")
