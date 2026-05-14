import io
import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def make_text_page(lines, width, height, font_name="Helvetica", font_size=12, left_margin=40, top_margin=40, line_spacing=14):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))

    try:
        pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))
        font_name = "DejaVuSans"
    except Exception:
        pass

    c.setFont(font_name, font_size)
    y = height - top_margin
    for line in lines:
        c.drawString(left_margin, y, line)
        y -= line_spacing
        if y < 0:
            break

    c.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf.pages[0]


def replace_pdf_line_in_pdf(input_pdf_path, output_pdf_path, page_number, line_number, new_text):
    reader = PdfReader(input_pdf_path)
    if page_number < 0 or page_number >= len(reader.pages):
        raise ValueError(f"Page number {page_number + 1} is out of range.")

    page = reader.pages[page_number]
    text = page.extract_text()
    if text is None:
        raise ValueError("Could not extract text from the selected page.")

    lines = text.splitlines()
    if line_number < 0 or line_number >= len(lines):
        raise ValueError(f"Line number {line_number + 1} is out of range for page {page_number + 1}.")

    lines[line_number] = new_text

    media_box = page.mediabox
    width = float(media_box.width)
    height = float(media_box.height)

    modified_page = make_text_page(lines, width, height)

    writer = PdfWriter()
    for i, original_page in enumerate(reader.pages):
        if i == page_number:
            writer.add_page(modified_page)
        else:
            writer.add_page(original_page)

    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Saved modified PDF to: {output_pdf_path}")


def split_pdf_pages_to_named_files(input_pdf_path, output_dir=None):
    reader = PdfReader(input_pdf_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        lines = text.splitlines()
        if len(lines) > 8:
            name = lines[8].strip()
        else:
            name = f"page_{i + 1}"

        invalid_chars = r"\/:*?\"<>|"
        safe_name = "".join(ch for ch in name if ch not in invalid_chars).strip()
        if not safe_name:
            safe_name = f"page_{i + 1}"

        output_filename = f"{safe_name}.pdf"
        if output_dir:
            output_filename = os.path.join(output_dir, output_filename)

        writer = PdfWriter()
        writer.add_page(page)
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

        print(f"Created: {output_filename}")
