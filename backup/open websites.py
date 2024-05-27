import webbrowser

# Define an array of website links
links = [
"https://imgmak.com/image/lFNZm",
"https://imgmak.com/image/lFAAU",
"https://imgmak.com/image/lFYJN",
"https://imgmak.com/image/lF54h",
"https://imgmak.com/image/lFbPa",
"https://imgmak.com/image/lFC3v",
"https://imgmak.com/image/lFIoJ",

]

# Open each link in a new browser tab
for link in links:
    webbrowser.open_new_tab(link)
