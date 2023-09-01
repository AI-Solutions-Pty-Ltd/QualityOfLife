import os
import subprocess

def open_print_dialog_with_adobe_reader(pdf_path):
    adobe_reader_path = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"  # Replace with the actual path to AcroRd32.exe
    subprocess.Popen([adobe_reader_path, "/p", pdf_path], shell=True)

def open_print_dialog_for_all_pdfs_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            open_print_dialog_with_adobe_reader(pdf_path)
            print(f"Print dialog opened for {pdf_path}.")

if __name__ == "__main__":
    target_directory = r"H:\My Drive\1. GME\Salaries\2023\IRP5\Re-submitted\gme emp501"
    open_print_dialog_for_all_pdfs_in_directory(target_directory)



