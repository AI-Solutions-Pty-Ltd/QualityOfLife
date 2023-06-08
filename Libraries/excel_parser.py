import pandas as pd
import io
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def parse_excel_gui(tab_control):
    def parse_excel_data():
        excel_data = excel_text.get("1.0", tk.END)
        parse_excel(excel_data)
    second_tab = ttk.Frame(tab_control)
    tab_control.add(second_tab, text="Excel Parser")

    excel_label = tk.Label(second_tab, text="Paste Excel data:")
    excel_label.pack()
    excel_text = tk.Text(second_tab, height=10, width=50)
    excel_text.pack()

    parse_button = tk.Button(second_tab, text="Parse Excel", command=parse_excel_data)
    parse_button.pack()

def parse_excel(excel_data):
    try:
        df = pd.read_csv(io.StringIO(excel_data), delimiter="\t")

        # Make changes to the data
        df['Batch Name'] = df.apply(lambda row: "OWNER " + row['Property'].split(maxsplit=1)[1], axis=1)
        df['Owner name'] = df.apply(lambda row: row['Owner'].split(" - ")[1].split(maxsplit=1)[1].strip(), axis=1)
        df['Bank'] = df['BANK']
        df['Account Number'] = df['ACC NUMBER']
        df['Their Reference'] = df.apply(lambda row: "GME " + row['Property'].split(maxsplit=1)[1] + " RENT", axis=1)
        df['My Reference'] = df.apply(lambda row: "OWN" + row['Owner'].split(" - ")[0][3:].lstrip('0') + " " + row['Property'].split(maxsplit=1)[1], axis=1)
        df['Amount'] = df['Amount'].abs()
        df['Email'] = "CHANTELLEP@GARYMANNESTATES.CO.ZA"
        df['POP reference'] = df.apply(lambda row: "POP OWN" + row['Owner'].split(" - ")[0][3:].lstrip('0') + " " + row['Property'].split(maxsplit=1)[1], axis=1)

        # Select only the required columns
        df = df[['Batch Name', 'Owner name', 'Bank', 'Account Number', 'Their Reference', 'My Reference', 'Amount', 'Email', 'POP reference']]

        save_file_dialog = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

        if save_file_dialog:
            df.to_excel(save_file_dialog, index=False)
            messagebox.showinfo("Success", "Excel file created successfully!")
        else:
            messagebox.showwarning("Warning", "No file selected. Excel file not created.")
    except pd.errors.ParserError:
        messagebox.showerror("Error", "Invalid data format!")
