import pandas as pd
from bs4 import BeautifulSoup
import os
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

def parse_html_gui(tab_control):
    def parse_html_data():
        excel_data = excel_text.get("1.0", tk.END)
        excel_text.delete("1.0", tk.END)
        extract_table_to_excel(excel_data)
    
        
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text="HTML Parser")

    excel_label = tk.Label(tab, text="Paste HTML data:")
    excel_label.pack()
    excel_text = tk.Text(tab, height=10, width=50)
    excel_text.pack()
        
    parse_button = tk.Button(tab, text="Parse HTML", command=parse_html_data)
    parse_button.pack()
    
def extract_table_to_excel(html_table):
    # Parse the HTML table with BeautifulSoup
    # try:
        print("starting")
        soup = BeautifulSoup(html_table, 'html.parser')
        table = soup.find('table')
        
        # Extract the table headers
        headers = []
        for th in table.find_all('th'):
            colspan = int(th.get('colspan', 1))
            header_text = th.text.strip()
            headers.extend([f"{header_text} {i}" for i in range(1, colspan + 1)])

        # Extract the table data
        data = []
        for row in table.find_all('tr'):
            row_data = []
            for td in row.find_all('td'):
                # Check if the <td> contains an <input> element with checkbox
                input_elem = td.find('input', {
                    'type': 'checkbox',
                    'checked': 'True',
                    })
                if input_elem:
                    row_data.append(True)
                else:
                    input_elem = td.find('input', {
                        'type': 'checkbox',
                        })
                    if input_elem:
                        row_data.append(False)
                    else:
                        row_data.append(td.text.strip())
                    # Otherwise, add the text content of the <td>
            if row_data:
                data.append(row_data)
                
        print('data extracted')
        # Create a DataFrame using pandas
        df = pd.DataFrame(data, columns=headers)

        today = datetime.date.today().strftime("%Y-%m-%d")
        save_file_dialog = filedialog.asksaveasfilename(
            defaultextension=".xlsx", 
            filetypes=[("Excel Files", "*.xlsx")], 
            initialfile=f"{today}-html-table.xlsx"
            )

        if save_file_dialog:
            df.to_excel(save_file_dialog, index=False)
            messagebox.showinfo("Success", "Excel file created successfully!")
            os.startfile(save_file_dialog)
            
    # except pd.errors.ParserError:
        # messagebox.showerror("Error", "Invalid data format!")
