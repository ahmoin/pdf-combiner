import PyPDF2
import os

def combine_pdfs(input_folder, output_file):
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]
    pdf_files.sort()
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_file in pdf_files:
        with open(os.path.join(input_folder, pdf_file), "rb") as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    with open(output_file, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == "__main__":
    input_folder = "pdfs"
    output_file = "combined.pdf"

    combine_pdfs(input_folder, output_file)

    print(f"PDF files in {input_folder} combined into {output_file}")
