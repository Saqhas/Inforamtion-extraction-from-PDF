from PyPDF2 import PdfFileWriter, PdfFileReader

# Reading the PDF
PDF_PATH = "data/input.pdf"
pdf_doc = PdfFileReader(open(PDF_PATH, "rb"))

# Extraction document inforamtion
print("---------------PDF's info---------------")
print(pdf_doc.documentInfo)
print("PDF is encrypted: " + str(pdf_doc.isEncrypted))
print("---------------Number of pages---------------")
print(pdf_doc.numPages)

# Splitting document page by page
pdf_page_1 = pdf_doc.getPage(0)
pdf_page_4 = pdf_doc.getPage(3)
print(pdf_page_1)
print(pdf_page_4)

# Extraction text from a Page
text = pdf_page_1.extractText()
print(text[:500])

# Merging documents page by page
new_pdf = PdfFileWriter()
new_pdf.addPage(pdf_page_1)
new_pdf.addPage(pdf_page_4)
new_pdf.write(open("new_pdf.pdf", "wb"))
print(new_pdf)


# Cropping pages
print("Upper Left: ", pdf_page_1.cropBox.getUpperLeft())
print("Lower Right: ", pdf_page_1.cropBox.getLowerRight())

x1, y1 = 0, 550
x2, y2 = 612, 320

cropped_page = pdf_page_1
cropped_page.cropBox.upperLeft = (x1, y1)
cropped_page.cropBox.lowerRight = (x2, y2)

cropped_pdf = PdfFileWriter()
cropped_pdf.addPage(cropped_page)
cropped_pdf.write(open("cropped.pdf", "wb"))


# Encripting and decripting the pdf files
PASSWORD = "password_123"
encrypted_pdf = PdfFileWriter()
encrypted_pdf.addPage(pdf_page_1)
encrypted_pdf.encrypt(PASSWORD)
encrypted_pdf.write(open("encrypted_pdf.pdf", "wb"))

read_encrypted_pdf = PdfFileReader(open("encrypted_pdf.pdf", "rb"))
print(read_encrypted_pdf.isEncrypted)
if read_encrypted_pdf.isEncrypted:
    read_encrypted_pdf.decrypt(PASSWORD)
print(read_encrypted_pdf.documentInfo)



