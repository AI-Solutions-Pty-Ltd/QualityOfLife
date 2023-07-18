import pandas as pd
from bs4 import BeautifulSoup
import os
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def parse_fnb_html_gui(tab_control):
    def parse_html_data():
        excel_data = excel_text.get("1.0", tk.END)
        excel_text.delete("1.0", tk.END)
        extract_data_from_html_fnb(excel_data)
    
        
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text="FNB Parser")

    excel_label = tk.Label(tab, text="Paste FNB data:")
    excel_label.pack()
    excel_text = tk.Text(tab, height=10, width=50)
    excel_text.pack()
        
    parse_button = tk.Button(tab, text="Parse FNB", command=parse_html_data)
    parse_button.pack()


def extract_data_from_html_fnb(html_data):
    print('extracting fnb')
    soup = BeautifulSoup(html_data, 'html.parser')

    # Find all the rows containing table data
    rows = soup.find_all('div', class_='tableDataRow tableRowGroup1 clearfix')

    # Initialize lists to store the extracted data
    names = []
    dates = []
    payment_methods = []
    totals = []
    statuses = []

    # Extract the relevant data from each row
    for row in rows:
        name = row.find('div', class_='tableCell col1').text.strip()
        date = row.find('div', class_='tableCell col2').text.strip()
        payment_method = row.find('div', class_='tableCell col2').find_next('div').text.strip()
        total = row.find('div', class_='tableCell col3 right').text.strip()
        status = row.find('div', class_='tableCell col4').text.strip()

        names.append(name)
        dates.append(date)
        payment_methods.append(payment_method)
        totals.append(total)
        statuses.append(status)

    # Create a DataFrame using pandas
    data = {
        'Name': names,
        'Details - Date': dates,
        'Details - Payment Method': payment_methods,
        'Total': totals,
        'Status': statuses
    }
    df = pd.DataFrame(data)

    today = datetime.date.today().strftime("%Y-%m-%d")
    save_file_dialog = filedialog.asksaveasfilename(
        defaultextension=".xlsx", 
        filetypes=[("Excel Files", "*.xlsx")], 
        initialfile=f"{today}-html-table.xlsx"
        )
    print(df)
    if save_file_dialog:
        df.to_excel(save_file_dialog, index=False)
        messagebox.showinfo("Success", "Excel file created successfully!")
        os.startfile(save_file_dialog)

