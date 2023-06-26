import tkinter as tk
import pikepdf
from tkinter import ttk, filedialog, messagebox
import glob
import threading
import os

# Tab 4 - PDF PWd remover
def remove_pwd_gui(tab_control):
    def select_pdf_folder():
        file_names = filedialog.askopenfilenames()
        if file_names:
            password = password_entry.get()
            remove_password(file_names, password)

    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text="PDF Password Remover")

    # Password Entry
    password_label = tk.Label(tab, text="Enter Password:")
    password_label.pack()

    password_entry = tk.Entry(tab, show="*")
    password_entry.pack()

    export_pdf_button = tk.Button(
        tab, 
        text="Select PDF to remove password", 
        command=select_pdf_folder
    )
    export_pdf_button.pack()

    
def remove_password(file_names, pwd):
    for file in file_names:
        pdf_file = glob.glob(file)[0]
        pdf_pass = pwd or "748840834"
        with pikepdf.open(pdf_file, password=pdf_pass) as pdf:
            output_filename = f"{os.path.splitext(pdf_file)[0]}-password-removed.pdf"
            pdf.save(output_filename)
            print(f"Password removed for {pdf_file}. Output file: {output_filename}")
