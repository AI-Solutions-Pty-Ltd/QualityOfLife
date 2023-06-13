import webbrowser
import tkinter as tk
from tkinter import ttk
import subprocess
import time
import sys
import pyautogui
from pywinauto import Application

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
    
def activate_and_kill_chrome():
    app = Application().connect(title_re=".*Chrome.*")
    chrome_window = app.top_window()
    chrome_window.set_focus()
    pyautogui.hotkey("Ctrl", "w")
        
def open_whatsapp_chat(number):
    whatsapp_number = "+27" + number[1:]
    whatsapp_url = f"https://wa.me/{whatsapp_number}"
    
    subprocess.Popen(["start", "", whatsapp_url], shell=True)

    time.sleep(3)
    activate_and_kill_chrome()

def open_website(number):
    if len(number) >= 10 and number.startswith("0"):
        open_whatsapp_chat(number)
    else:
        print("Invalid number. Please enter a valid South African number.")
