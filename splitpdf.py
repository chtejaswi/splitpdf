import pandas as pd
from PyPDF2 import PdfReader, PdfWriter

# Step 1: Read the CSV file and extract the "NAME" column values to a list
csv_file_path = 'C:\\Users\\chunduri.t\\Downloads\\input\\Names.csv'
df = pd.read_csv(csv_file_path)
name_list = df['NAME'].tolist()

# Step 2: Split the input PDF file and create multiple output PDF files
input_pdf_path = 'C:\\Users\\chunduri.t\\Downloads\\input\\22799.pdf'
output_folder = 'C:\\Users\\chunduri.t\\Downloads\\splitpdf\\'

# Step 3: Split the input PDF file and create individual output PDF files
with open(input_pdf_path, 'rb') as file:
    pdf_reader = PdfReader(file)
    total_pages = len(pdf_reader.pages)

    # Iterate through the list and create individual output PDF files
    for i, name in enumerate(name_list):
        output_pdf_path = f'{output_folder}{name}.pdf'  # Output file path for each item in the list

        # Create a new PDF writer
        pdf_writer = PdfWriter()

        # Add one page from the original PDF (customize this based on your needs)
        pdf_writer.add_page(pdf_reader.pages[i % total_pages])
        pdf_writer.add_page(pdf_reader.pages[-1])

        # Write the output PDF file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f'Successfully created {output_pdf_path}')