from pdf_helpers import *

input_pdf = "شمس بنت سالم السهيلية.pdf"
new = 'test'
# split_pdf_pages_to_named_files(input_pdf)

replace_pdf_line_in_pdf(input_pdf, "output.pdf", 0, 8, new)