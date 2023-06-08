import tkinter as tk
from tkinter import ttk

from pypdf import PdfReader, PdfWriter
from tkinter import filedialog
from tkinter import messagebox
import os

# Tab 3 - PDF Exporter
def export_pdf_gui(tab_control):
    def export_pdf():
        num_pages = int(num_pages_entry.get())
        if num_pages > 0:
            select_pdf_file(num_pages)
        else:
            messagebox.showerror("Error", "Must be more than zero!")
            
    third_tab = ttk.Frame(tab_control)
    tab_control.add(third_tab, text="PDF Splitter")

    export_label = tk.Label(third_tab, text="Select PDF to split:")
    export_label.pack()

    num_pages_label = tk.Label(third_tab, text="Number of Pages to Split:")
    num_pages_label.pack(pady=5)

    num_pages_entry = tk.Entry(third_tab)
    num_pages_entry.pack(pady=5)
    num_pages_entry.bind("<Return>", export_pdf)

    export_pdf_button = tk.Button(third_tab, text="Export PDF Pages", command=export_pdf)
    export_pdf_button.pack()

def select_pdf_file(number):
    filepath = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")]
    )
    if filepath:
        export_pages(filepath, number)

def export_pages(pdf_path, number):
    input_pdf = PdfReader(pdf_path)
    
    output_folder = "./output"
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            
    page_number = 0
    split = 0
    output_pdf = None
    start = 1
    for page in input_pdf.pages:
        page_number += 1
        split += 1
        if not output_pdf:
            output_pdf = PdfWriter()
        output_pdf.add_page(page)
        
        if page_number == 30:
            x = 1
        if split == number:
            split = 0
            if number == 1:
                path = f"{output_folder}/{page_number}.pdf"
            else:
                path = f"{output_folder}/{start} - {page_number}.pdf"
            
            output_pdf.write(path)
            
            start = page_number + 1
            output_pdf = None
        elif page_number == len(input_pdf.pages): 
            if number == 1:
                path = f"{output_folder}/{page_number}.pdf"
            else:
                path = f"{output_folder}/{start} - {page_number}.pdf"

            output_pdf.write(path)
            output_pdf = None
            
    messagebox.showinfo("Success", "Pdf files exported successfully!")