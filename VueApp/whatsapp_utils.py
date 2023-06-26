import webbrowser
from pyscript import Element

def open_whatsapp_chat(number):
    # Remove leading zero and add "+27"
    whatsapp_number = "+27" + number[1:]
    # WhatsApp URL format: https://wa.me/<number>
    whatsapp_url = f"https://wa.me/{whatsapp_number}"
    webbrowser.open(whatsapp_url)

def open_website():
    number = Element("whatsapp_number").element.value
    
    if len(number) >= 10 and number.startswith("0"):
        open_whatsapp_chat(number)
    else:
        print("Invalid number. Please enter a valid South African number.")
