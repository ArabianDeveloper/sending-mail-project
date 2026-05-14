from pypdf import PdfReader, PdfWriter
reader = PdfReader("دورة مشكاة ( اناث ).pdf")


# for page in reader.pages:
#     print("="*10 + f"{reader.pages.index(page) + 1}" + "="*10)
#     pagecontent = page.extract_text().splitlines()
#     print(pagecontent[8].strip())
#     # for line in pagecontent:
#     #     print(line + str(pagecontent.index(line)))



for i, page in enumerate(reader.pages):
    print("="*10 + f"{reader.pages.index(page) + 1}" + "="*10)
    pagecontent = page.extract_text().splitlines()
    name = pagecontent[8].strip()
    
    writer = PdfWriter()
    writer.add_page(page)
    
    output_filename = f"{name}.pdf"
    with open(output_filename, "wb") as output_pdf:
        writer.write(output_pdf)
    print(f"Created: {output_filename}")