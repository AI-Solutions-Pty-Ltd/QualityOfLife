import tkinter as tk
from tkinter import ttk

from pypdf import PdfWriter
from tkinter import filedialog
from tkinter import messagebox
import os

# Tab 3 - PDF Exporter
def combine_pdf_gui(tab_control):
    def button_press():
        select_pdf_files()
            
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text="Combined PDFs")

    export_label = tk.Label(tab, text="Select PDFs to combine:")
    export_label.pack()

    export_pdf_button = tk.Button(tab, text="Combine", command=button_press)
    export_pdf_button.pack()

def select_pdf_files():
    filepaths = filedialog.askopenfilenames(
        filetypes=[("PDF files", "*.pdf")]
    )
    if filepaths:
        combine_pdfs(filepaths)

def combine_pdfs(files):
    merger = PdfWriter()

    for pdf in files:
        print(pdf)
        merger.append(pdf)
    folder = os.path.dirname(files[0])
    merger.write(f"{folder}/merged-pdf.pdf")
    merger.close()

    messagebox.showinfo("Success", "Pdf files successfully combined!")
    return
