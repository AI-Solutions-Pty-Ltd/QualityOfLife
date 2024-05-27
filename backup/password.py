import pikepdf
import os
import glob
import tkinter as tk
from tkinter import ttk

from pypdf import PdfReader, PdfWriter
from tkinter import filedialog
from tkinter import messagebox
import os

# Tab 3 - PDF Exporter
def export_pdf_gui(tab_control):
    def export_pdf():
        select_pdf_file()
     
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text="PDF Password Remover")

    export_label = tk.Label(tab, text="Select PDF to remove password:")
    export_label.pack()

    export_pdf_button = tk.Button(tab, text="Export PDF Pages", command=export_pdf)
    export_pdf_button.pack()

def select_pdf_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")]
    )
    if filepath:
        remove_password(filepath)
    
def remove_password(folder_path):
    save_path = f"{folder_path}/password_removed/"
    pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))

    pdf_pass = "748840834"
    counter = 0
    for pdf_file in pdf_files:
        counter += 1
        with pikepdf.open(pdf_file, password=pdf_pass) as pdf:
            pdf.save(f"{save_path}/{counter}.pdf")
