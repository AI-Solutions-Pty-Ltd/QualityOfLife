import webbrowser

# Define an array of website links
links = [
    {"prop": "PRO00001","own":"OWN00001"},
    {"prop": "PRO00487","own":"OWN00108"},
    {"prop": "PRO00622","own":"OWN00169"},
    {"prop": "PRO00561","own":"OWN00137"},
    {"prop": "PRO00651","own":"OWN00187"},
    {"prop": "PRO00633","own":"OWN00176"},
    {"prop": "PRO00634","own":"OWN00177"},
    {"prop": "PRO00605","own":"OWN00156"},
    {"prop": "PRO00642","own":"OWN00184"},
    {"prop": "PRO00486","own":"OWN00107"},
    {"prop": "PRO00103","own":"OWN00002"},
    {"prop": "PRO00631","own":"OWN00174"},
    {"prop": "PRO00005","own":"OWN00029"},
    {"prop": "PRO00006","own":"OWN00060"},
    {"prop": "PRO00008","own":"OWN00039"},
    {"prop": "PRO00010","own":"OWN00064"},
    {"prop": "PRO00652","own":"OWN00188"},
    {"prop": "PRO00086","own":"OWN00054"},
    {"prop": "PRO00088","own":"OWN00009"},
    {"prop": "PRO00089","own":"OWN00054"},
    {"prop": "PRO00183","own":"OWN00068"},
    {"prop": "PRO00578","own":"OWN00142"},
    {"prop": "PRO00202","own":"OWN00046"},
    {"prop": "PRO00249","own":"OWN00055"},
    {"prop": "PRO00553","own":"OWN00132"},
]

# Open each link in a new browser tab
for link in links:
    link = f"https://rms.propertysuite.co.za/Owners/Owner.aspx?OwnerID={link['own']}&PID={link['prop']}"
    link = f"javascript:__doPostBack('ctl00$MainContent$FormView1$FormView2$StatementLink','')"
    webbrowser.open_new_tab(link)