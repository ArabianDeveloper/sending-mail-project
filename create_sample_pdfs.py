"""
Generate sample PDF files for testing email attachments.
Run this script to create test PDFs in a 'pdfs' folder.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path
import csv
import openpyxl

def load_data(file_path):
    pdfs_name = []
    try:
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)[:10]

        for row in rows:
            pdfs_name.append(row['Name'])
        
        return pdfs_name
    except Exception as e:
        print(f"Error loading data: {e}")

def create_sample_pdfs():
    # Create pdfs folder if it doesn't exist
    pdf_folder = Path("pdfs")
    pdf_folder.mkdir(exist_ok=True)

    
    for name in load_data("Untitled spreadsheet - Sheet1.csv"):
        pdf_path = pdf_folder / f"{name}.pdf"

        # Create PDF
        c = canvas.Canvas(str(pdf_path), pagesize=letter)
        width, height = letter
        
        # Add content
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, height - 50, "Sample Report")
        
        c.setFont("Helvetica", 12)
        c.drawString(50, height - 100, f"Name: {name}")
        c.drawString(50, height - 160, f"Report Date: 2024")
        c.drawString(50, height - 200, "This is a sample PDF file for email attachment testing.")
        
        c.save()
        print(f"✓ Created: {pdf_path}")
    
    print(f"\n✓ All {len(load_data('Untitled spreadsheet - Sheet1.csv'))} PDF files created in '{pdf_folder}/' folder")
    print("Now you can use these files for testing email attachments!")


if __name__ == "__main__":
    try:
        create_sample_pdfs()
        print(load_data("Untitled spreadsheet - Sheet1.csv"))
    except ImportError:
        print("Error: reportlab is not installed")
        print("Install it with: pip install reportlab")
    except Exception as e:
        print(f"Error: {e}")
