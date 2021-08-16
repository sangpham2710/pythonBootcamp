# import csv

# with open('example.csv', encoding='utf-8') as data:
#     csv_data = csv.reader(data)
#     data_lines = list(csv_data)
#     print(data_lines)

# with open('to_save_file.csv', mode='w', newline='', encoding='utf-8') as f:
#     csv_writer = csv.writer(f, delimiter=',')
#     csv_writer.writerows(data_lines)

# import PyPDF2
# with open('Working_Business_Proposal.pdf', 'rb') as f:
#     pdf_reader = PyPDF2.PdfFileReader(f)
#     pdf_writer = PyPDF2.PdfFileWriter()
#     pdf_writer.addPage(pdf_reader.getPage(0))
#     with open('Some_BrandNew_Doc.pdf', 'wb') as f:
#         pdf_writer.write(f)

#     page_one_text = pdf_reader.getPage(0).extractText()
#     print(page_one_text)
