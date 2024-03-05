import pandas as pd
import io
import os
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import webbrowser


def parse_excel_gui(tab_control):
    def parse_excel_data():
        checkbox_value = open_statements_var.get()
        excel_data = excel_text.get("1.0", tk.END)
        parse_excel(excel_data, checkbox_value)

    second_tab = ttk.Frame(tab_control)
    tab_control.add(second_tab, text="Excel Parser")

    excel_label = tk.Label(second_tab, text="Paste Excel data:")
    excel_label.pack()
    excel_text = tk.Text(second_tab, height=10, width=50)
    excel_text.pack()

    open_statements_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(
        second_tab, text="Open Statements", variable=open_statements_var
    )
    checkbox.pack()

    parse_button = tk.Button(second_tab, text="Parse Excel", command=parse_excel_data)
    parse_button.pack()


def parse_excel(excel_data, checkbox_value):
    df = pd.read_csv(io.StringIO(excel_data), delimiter="\t")
    df.columns = df.columns.str.lower().str.strip()  # Lowercase the column names and remove leading/trailing whitespaces
    if checkbox_value:
        for index, row in df.iterrows():
            owner = row["owner"][:8]
            property = row["property"][:8]
            web_url = f"https://rms.propertysuite.co.za/Route/?d=stmt&tp=own&o={owner}&p={property}"
            webbrowser.open_new_tab(web_url)

    df["batch name"] = df.apply(lambda row: "OWNER " + row["property"].split(maxsplit=1)[1], axis=1)

    df["owner name"] = df.apply(lambda row: row["owner"].split(" - ")[1].split(maxsplit=1)[1].strip(), axis=1)

    df["account number"] = df["acc num"] if "acc num" in df else df["acc number"] if "acc number" in df else df["bank acc"]

    df["their reference"] = df.apply(lambda row: "GME " + row["property"].split(maxsplit=1)[1] + " RENT", axis=1)
    df["my reference"] = df.apply(lambda row: "OWN" + row["owner"].split(" - ")[0][3:].lstrip("0") + " " + row["property"].split(maxsplit=1)[1], axis=1)
    
    df["amount"] = df["amount"].str.replace(',', '')
    df["amount"] = pd.to_numeric(df["amount"], errors='coerce').abs()


    df["email"] = "chantellep@garymannestates.co.za"
    df["pop reference"] = df.apply(lambda row: "POP OWN" + row["owner"].split(" - ")[0][3:].lstrip("0") + " " + row["property"].split(maxsplit=1)[1], axis=1)

    df = df[["batch name", "owner name", "bank", "account number", "their reference", "my reference", "amount", "email", "pop reference"]]

    today = datetime.date.today().strftime("%Y-%m-%d")
    save_file_dialog = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")], initialfile=f"{today}.xlsx")

    if save_file_dialog:
        df.to_excel(save_file_dialog, index=False)
        messagebox.showinfo("Success", "Excel file created successfully!")
        os.startfile(save_file_dialog)
    else:
        messagebox.showwarning("Warning", "No file selected. Excel file not created.")
