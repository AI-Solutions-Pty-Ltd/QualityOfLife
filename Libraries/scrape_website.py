import pyperclip
import json

import csv
import requests
from bs4 import BeautifulSoup
# from generate_pdf import generate_pdf

tenants = [
 {
   "Property #": "PRO00440",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00372"
 },
 {
   "Property #": "PRO00040",
   "Owner #": "OWN00007",
   "Tenant #": "TEN00209"
 },
 {
   "Property #": "PRO00040",
   "Owner #": "OWN00007",
   "Tenant #": "TEN00589"
 },
 {
   "Property #": "PRO00041",
   "Owner #": "OWN00007",
   "Tenant #": "TEN00140"
 },
 {
   "Property #": "PRO00041",
   "Owner #": "OWN00007",
   "Tenant #": "TEN00474"
 },
 {
   "Property #": "PRO00041",
   "Owner #": "OWN00007",
   "Tenant #": "TEN00579"
 },
 {
   "Property #": "PRO00041",
   "Owner #": "OWN00007",
   "Tenant #": "TEN00642"
 },
 {
   "Property #": "PRO00061",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00060"
 },
 {
   "Property #": "PRO00601",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00626"
 },
 {
   "Property #": "PRO00063",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00088"
 },
 {
   "Property #": "PRO00626",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00614"
 },
 {
   "Property #": "PRO00457",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00371"
 },
 {
   "Property #": "PRO00252",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00361"
 },
 {
   "Property #": "PRO00375",
   "Owner #": "OWN00080",
   "Tenant #": "TEN00361"
 },
 {
   "Property #": "PRO00250",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00212"
 },
 {
   "Property #": "PRO00460",
   "Owner #": "OWN00080",
   "Tenant #": "TEN00383"
 },
 {
   "Property #": "PRO00253",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00059"
 },
 {
   "Property #": "PRO00376",
   "Owner #": "OWN00080",
   "Tenant #": "TEN00059"
 },
 {
   "Property #": "PRO00604",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00629"
 },
 {
   "Property #": "PRO00378",
   "Owner #": "OWN00080",
   "Tenant #": "TEN00049"
 },
 {
   "Property #": "PRO00258",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00005"
 },
 {
   "Property #": "PRO00603",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00628"
 },
 {
   "Property #": "PRO00259",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00147"
 },
 {
   "Property #": "PRO00255",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00364"
 },
 {
   "Property #": "PRO00260",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00022"
 },
 {
   "Property #": "PRO00260",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00408"
 },
 {
   "Property #": "PRO00261",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00072"
 },
 {
   "Property #": "PRO00262",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00005"
 },
 {
   "Property #": "PRO00262",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00437"
 },
 {
   "Property #": "PRO00264",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00005"
 },
 {
   "Property #": "PRO00602",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00627"
 },
 {
   "Property #": "PRO00515",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00436"
 },
 {
   "Property #": "PRO00590",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00600"
 },
 {
   "Property #": "PRO00491",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00371"
 },
 {
   "Property #": "PRO00492",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00371"
 },
 {
   "Property #": "PRO00596",
   "Owner #": "OWN00079",
   "Tenant #": "TEN00502"
 }
]

cookies = {
    "ASP.NET_SessionId": "4qnn4fbnifxgiyk1ldqgeoro",
}

start_date = '01032022'
end_date = '28022023'

def open_urls_in_browser(tenants):
    data = []
    for tenant in tenants:
        ten = tenant['Tenant #']
        pro = tenant['Property #']
        owner = tenant['Owner #']
        tenant_data = {
            "Tenant": ten,
            "Property": pro,
            "Owner": owner,
            "Transactions": [],
        }
        print(ten, pro, owner)
        # url = f"https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID={ten}&PID={pro}&OID={owner}&STD={start_date}&EDD={end_date}"
        url = f"https://rms.propertysuite.co.za/Reports/Owners/OwnerMonthly.aspx?OID={owner}&PID={pro}&TID={ten}&STD={start_date}&EDD={end_date}&IFD=YES&SHOW=NO&EDIT=NO"
        page = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(page.content, "html.parser")
        
        # elements = soup.find_all(lambda tag: tag.name == 'div' and tag.get('style') == ' font-size:larger; font-weight:bold ; text-decoration:underline ')
        # for element in elements:
        #     element.extract()
        # elements = soup.find_all('link', href='https://rms.propertysuite.co.za/stylesheets/Reports_02.css?v=005')
        # for element in elements:
        #     element.extract()
        # form = soup.find("form")
        # generate_pdf(form.prettify(), owner, ten, pro, start_date, end_date)
        # results = soup.find(id="aspnetForm")
        tables = soup.find_all("table", class_="table_report")
        
        count = 0

        for table in tables:
            if count == 2:
                owner_statement = table
            if count == 4:
                tenant_statement = table
            count += 1
        
        data = extract_transactions(data, owner_statement, ten, pro, owner, "owner")
        data = extract_transactions(data, tenant_statement, ten, pro, owner, "tenant")


    data_json = json.dumps(data, indent=1)
    pyperclip.copy(data_json)

    # save to csv file
    with open(f"transactions.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["type", "tenant", "property", "owner", "ContraAcc", "date", "description", "amount", "balance"])
        writer.writerows(data)

def extract_transactions(data, statement, tenant, property, owner, type):
    rows = statement.find_all("tr")
    count = 0
    for row in rows:
        count += 1
        if count < 3: # 1st and 2nd row are headers
            continue
        
        cols = row.find_all("td")
        
        if cols[1].get_text() == "No Data for Selected Period":
            transaction = {
                "type": type,
                "tenant": tenant,
                "property": property,
                "owner": owner,
                "ContraAcc": "",
                "date" : "",
                "description" : "no transactions found",
                "amount" : 0,
                "balance" : "",
            }
            data.append(transaction)
            return data
        
        contra = cols[0].get_text(separator='|')
        contra_cols = contra.split('|')
        contra_acc_value = contra_cols[4].split(':')[-1].strip()

        dt = cols[3].get_text().replace(",","")
        ct = cols[4].get_text().replace(",","")

        if dt and dt != "\xa0":
            amount = float(dt)
        elif ct and ct != "\xa0":
            amount = -float(ct)
        else:
            raise ValueError("No amount found")
        transaction = {
            "type": type,
            "tenant": tenant,
            "property": property,
            "owner": owner,
            "ContraAcc": contra_acc_value,
            "date" : cols[2].get_text(),
            "description" : cols[1].get_text(),
            "amount" : amount,
            "balance" : cols[5].get_text(),
        }
        data.append(transaction)

    return data
      
open_urls_in_browser(tenants)