import webbrowser
import tkinter as tk
from tkinter import ttk

def whatsapp_gui(tab_control):
    def open_whatsapp_and_chat(event=None):
        number = number_entry.get()
        open_whatsapp_chat(number)
    first_tab = ttk.Frame(tab_control)
    tab_control.add(first_tab, text="WhatsApp and Console")

    number_label = tk.Label(first_tab, text="Enter a number:")
    number_label.pack()
    number_entry = tk.Entry(first_tab)
    number_entry.pack()
    number_entry.bind("<Return>", open_whatsapp_and_chat)

    open_button = tk.Button(first_tab, text="Open WhatsApp Chat", command=open_whatsapp_and_chat)
    open_button.pack()
    
def open_whatsapp_chat(number):
    # Remove leading zero and add "+27"
    whatsapp_number = "+27" + number[1:]
    # WhatsApp URL format: https://wa.me/<number>
    whatsapp_url = f"https://wa.me/{whatsapp_number}"
    webbrowser.open(whatsapp_url)

def open_website(number):
    if len(number) >= 10 and number.startswith("0"):
        open_whatsapp_chat(number)
    else:
        print("Invalid number. Please enter a valid South African number.")
