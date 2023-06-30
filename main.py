import tkinter as tk
from tkinter import ttk

from Libraries.whatsapp_utils import whatsapp_gui
from Libraries.excel_parser import parse_excel_gui
from Libraries.export_pdf_pages import export_pdf_gui
from Libraries.password_remover import remove_pwd_gui
from Libraries.combine_pdf_pages import combine_pdf_gui

# Create the GUI window
window = tk.Tk()
window.title("App")
window.geometry("600x400")

# Create tabs
tab_control = ttk.Notebook(window)

# Tab 1 - WhatsApp and Console
whatsapp_gui(tab_control)

# Tab 2 - Excel Parser
parse_excel_gui(tab_control)

# Tab 3 - Pdf Splitter
export_pdf_gui(tab_control)

# Tab 4 - Pdf Pwd remover
remove_pwd_gui(tab_control)

# Tab 5 - Combine Pdf Pwd
combine_pdf_gui(tab_control)

tab_control.pack(expand=1, fill="both")
window.mainloop()
