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
    checkbox = tk.Checkbutton(second_tab, text="Open Statements", variable=open_statements_var)
    checkbox.pack()
        
    parse_button = tk.Button(second_tab, text="Parse Excel", command=parse_excel_data)
    parse_button.pack()
    
    

def parse_excel(excel_data, checkbox_value):
    print(checkbox_value)
    try:
        df = pd.read_csv(io.StringIO(excel_data), delimiter="\t")
        if checkbox_value:
            for index, row in df.iterrows():
                # Access row values using row['column_name']
                owner = row['Owner'][0:8]
                property = row['Property'][0:8]
                # web_url = f"https://rms.propertysuite.co.za/Owners/Owner.aspx?OwnerID={owner}&PID={property}"
                web_url = f"https://rms.propertysuite.co.za/Route/?d=stmt&tp=own&o={owner}&p={property}"
                webbrowser.open_new_tab(web_url)
            
        # Make changes to the data
        df['Batch Name'] = df.apply(lambda row: "OWNER " + row['Property'].split(maxsplit=1)[1], axis=1)
        
        try:
            df['Owner name'] = df.apply(lambda row: row['Owner'].split(" - ")[1].split(maxsplit=1)[1].strip(), axis=1)
        except:
            df['Owner'] = df.apply(lambda row: row['Owner'].split(" - ")[1].split(maxsplit=1)[1].strip(), axis=1)
            
        df['Bank'] = df['BANK']
        try:
            df['Account Number'] = df['ACC NUM']
        except:
            try:
                df['Account Number'] = df['ACC NUMBER']
            except:
                df['Account Number'] = df['BANK ACC']
                
        df['Their Reference'] = df.apply(lambda row: "GME " + row['Property'].split(maxsplit=1)[1] + " RENT", axis=1)
        df['My Reference'] = df.apply(lambda row: "OWN" + row['Owner'].split(" - ")[0][3:].lstrip('0') + " " + row['Property'].split(maxsplit=1)[1], axis=1)
        df['Amount'] = df['Amount'].abs()
        df['Email'] = "CHANTELLEP@GARYMANNESTATES.CO.ZA"
        df['POP reference'] = df.apply(lambda row: "POP OWN" + row['Owner'].split(" - ")[0][3:].lstrip('0') + " " + row['Property'].split(maxsplit=1)[1], axis=1)

        # Select only the required columns
        df = df[['Batch Name', 'Owner name', 'Bank', 'Account Number', 'Their Reference', 'My Reference', 'Amount', 'Email', 'POP reference']]

        today = datetime.date.today().strftime("%Y-%m-%d")
        save_file_dialog = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")], initialfile=f"{today}.xlsx")

        if save_file_dialog:
            df.to_excel(save_file_dialog, index=False)
            messagebox.showinfo("Success", "Excel file created successfully!")
            os.startfile(save_file_dialog)  # Open the saved Excel file
        else:
            messagebox.showwarning("Warning", "No file selected. Excel file not created.")
    except pd.errors.ParserError:
        messagebox.showerror("Error", "Invalid data format!")
