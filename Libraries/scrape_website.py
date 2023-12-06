import pyperclip
import json
import requests
from bs4 import BeautifulSoup
from generate_pdf import generate_pdf

steele = [
    {'Tenant':'TEN00005','Property':'PRO00258'},
    {'Tenant':'TEN00005','Property':'PRO00262'},
    {'Tenant':'TEN00005','Property':'PRO00264'},
    {'Tenant':'TEN00022','Property':'PRO00260'},
    {'Tenant':'TEN00028','Property':'PRO00251'},
    {'Tenant':'TEN00046','Property':'PRO00256'},
    {'Tenant':'TEN00059','Property':'PRO00253'},
    {'Tenant':'TEN00060','Property':'PRO00061'},
    {'Tenant':'TEN00063','Property':'PRO00263'},
    {'Tenant':'TEN00072','Property':'PRO00261'},
    {'Tenant':'TEN00088','Property':'PRO00063'},
    {'Tenant':'TEN00147','Property':'PRO00259'},
    {'Tenant':'TEN00212','Property':'PRO00250'},
    {'Tenant':'TEN00355','Property':'PRO00257'},
    {'Tenant':'TEN00361','Property':'PRO00252'},
    {'Tenant':'TEN00364','Property':'PRO00255'},
    {'Tenant':'TEN00371','Property':'PRO00412'},
    {'Tenant':'TEN00371','Property':'PRO00457'},
    {'Tenant':'TEN00371','Property':'PRO00489'},
    {'Tenant':'TEN00371','Property':'PRO00491'},
    {'Tenant':'TEN00372','Property':'PRO00440'},
    {'Tenant':'TEN00408','Property':'PRO00260'},
    {'Tenant':'TEN00408','Property':'PRO00261'},
    {'Tenant':'TEN00436','Property':'PRO00515'},
    {'Tenant':'TEN00437','Property':'PRO00262'},
    {'Tenant':'TEN00452','Property':'PRO00253'},
    {'Tenant':'TEN00497','Property':'PRO00259'},
    {'Tenant':'TEN00502','Property':'PRO00596'},
    {'Tenant':'TEN00534','Property':'PRO00250'},
    {'Tenant':'TEN00572','Property':'PRO00255'},
    {'Tenant':'TEN00600','Property':'PRO00590'},
    {'Tenant':'TEN00605','Property':'PRO00258'},
    {'Tenant':'TEN00619','Property':'PRO00252'},
    {'Tenant':'TEN00626','Property':'PRO00601'},
    {'Tenant':'TEN00627','Property':'PRO00602'},
    {'Tenant':'TEN00628','Property':'PRO00603'},
    {'Tenant':'TEN00629','Property':'PRO00604'},
]


realty = [
    {'Tenant':'TEN00009','Property': 'PRO00047'},
{'Tenant':'TEN00015','Property': 'PRO00051'},
{'Tenant':'TEN00024','Property': 'PRO00050'},
{'Tenant':'TEN00035','Property': 'PRO00053'},
{'Tenant':'TEN00040','Property': 'PRO00052'},
{'Tenant':'TEN00058','Property': 'PRO00307'},
{'Tenant':'TEN00058','Property': 'PRO00323'},
{'Tenant':'TEN00058','Property': 'PRO00338'},
{'Tenant':'TEN00077','Property': 'PRO00049'},
{'Tenant':'TEN00098','Property': 'PRO00317'},
{'Tenant':'TEN00128','Property': 'PRO00326'},
{'Tenant':'TEN00131','Property': 'PRO00304'},
{'Tenant':'TEN00159','Property': 'PRO00335'},
{'Tenant':'TEN00168','Property': 'PRO00334'},
{'Tenant':'TEN00174','Property': 'PRO00337'},
{'Tenant':'TEN00176','Property': 'PRO00339'},
{'Tenant':'TEN00177','Property': 'PRO00321'},
{'Tenant':'TEN00181','Property': 'PRO00330'},
{'Tenant':'TEN00187','Property': 'PRO00320'},
{'Tenant':'TEN00201','Property': 'PRO00315'},
{'Tenant':'TEN00225','Property': 'PRO00319'},
{'Tenant':'TEN00229','Property': 'PRO00046'},
{'Tenant':'TEN00238','Property': 'PRO00316'},
{'Tenant':'TEN00239','Property': 'PRO00336'},
{'Tenant':'TEN00247','Property': 'PRO00331'},
{'Tenant':'TEN00254','Property': 'PRO00312'},
{'Tenant':'TEN00255','Property': 'PRO00325'},
{'Tenant':'TEN00256','Property': 'PRO00311'},
{'Tenant':'TEN00263','Property': 'PRO00332'},
{'Tenant':'TEN00264','Property': 'PRO00329'},
{'Tenant':'TEN00265','Property': 'PRO00328'},
{'Tenant':'TEN00266','Property': 'PRO00338'},
{'Tenant':'TEN00269','Property': 'PRO00322'},
{'Tenant':'TEN00271','Property': 'PRO00314'},
{'Tenant':'TEN00276','Property': 'PRO00313'},
{'Tenant':'TEN00277','Property': 'PRO00310'},
{'Tenant':'TEN00279','Property': 'PRO00324'},
{'Tenant':'TEN00281','Property': 'PRO00309'},
{'Tenant':'TEN00282','Property': 'PRO00306'},
{'Tenant':'TEN00283','Property': 'PRO00318'},
{'Tenant':'TEN00284','Property': 'PRO00333'},
{'Tenant':'TEN00285','Property': 'PRO00327'},
{'Tenant':'TEN00287','Property': 'PRO00305'},
{'Tenant':'TEN00290','Property': 'PRO00308'},
{'Tenant':'TEN00303','Property': 'PRO00048'},
{'Tenant':'TEN00333','Property': 'PRO00045'},
{'Tenant':'TEN00371','Property': 'PRO00409'},
{'Tenant':'TEN00371','Property': 'PRO00441'},
{'Tenant':'TEN00375','Property': 'PRO00446'},
{'Tenant':'TEN00381','Property': 'PRO00454'},
{'Tenant':'TEN00384','Property': 'PRO00465'},
{'Tenant':'TEN00388','Property': 'PRO00313'},
{'Tenant':'TEN00388','Property': 'PRO00465'},
{'Tenant':'TEN00394','Property': 'PRO00313'},
{'Tenant':'TEN00405','Property': 'PRO00307'},
{'Tenant':'TEN00409','Property': 'PRO00338'},
{'Tenant':'TEN00411','Property': 'PRO00334'},
{'Tenant':'TEN00433','Property': 'PRO00316'},
{'Tenant':'TEN00434','Property': 'PRO00331'},
{'Tenant':'TEN00440','Property': 'PRO00309'},
{'Tenant':'TEN00440','Property': 'PRO00320'},
{'Tenant':'TEN00457','Property': 'PRO00307'},
{'Tenant':'TEN00461','Property': 'PRO00315'},
{'Tenant':'TEN00469','Property': 'PRO00337'},
{'Tenant':'TEN00479','Property': 'PRO00332'},
{'Tenant':'TEN00480','Property': 'PRO00323'},
{'Tenant':'TEN00482','Property': 'PRO00330'},
{'Tenant':'TEN00508','Property': 'PRO00317'},
{'Tenant':'TEN00530','Property': 'PRO00046'},
{'Tenant':'TEN00539','Property': 'PRO00323'},
{'Tenant':'TEN00555','Property': 'PRO00309'},
{'Tenant':'TEN00566','Property': 'PRO00319'},
{'Tenant':'TEN00573','Property': 'PRO00334'},
{'Tenant':'TEN00577','Property': 'PRO00315'},
{'Tenant':'TEN00623','Property': 'PRO00598'},
{'Tenant':'TEN00624','Property': 'PRO00446'},
{'Tenant':'TEN00624','Property': 'PRO00599'},
{'Tenant':'TEN00636','Property': 'PRO00333'},
{'Tenant':'TEN00649','Property': 'PRO00305'},
{'Tenant':'TEN00657','Property': 'PRO00330'},
{'Tenant':'TEN00664','Property': 'PRO00323'},


]

cookies = {
    "ASP.NET_SessionId": "sahrdltoktuc5qsxajmlw45m",
}

start_date = '28022022'
end_date = '28022022'
owner = 'OWN00069'

def open_urls_in_browser(tenants):
    data = []
    for tenant in tenants:
        tenant_data = {
            "Tenant": tenant['Tenant'],
            "Property": tenant['Property'],
            "Transactions": [],
        }
        ten = tenant['Tenant']
        pro = tenant['Property']
        url = f"https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID={ten}&PID={pro}&OID={owner}&STD={start_date}&EDD={end_date}"
        page = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(page.content, "html.parser")
        
        
        elements = soup.find_all(lambda tag: tag.name == 'div' and tag.get('style') == ' font-size:larger; font-weight:bold ; text-decoration:underline ')
        for element in elements:
            element.extract()

        # elements = soup.find_all('link', href='https://rms.propertysuite.co.za/stylesheets/Reports_02.css?v=005')
        # for element in elements:
        #     element.extract()
        form = soup.find("form")
        generate_pdf(form.prettify(), owner, ten, pro, start_date, end_date)
    #     results = soup.find(id="aspnetForm")
    #     tables = results.find_all("table", class_="table_report")
        
    #     count = 0
    #     statement = None
    #     for table in tables:
    #         count += 1
    #         if count == 4:
    #             statement = table
    #             break
        
    #     rows = statement.find_all("tr")
    #     count = 0
    #     for row in rows:
    #         count += 1
    #         if count < 3:
    #             continue
    #         cols = row.find_all("td")
    #         dt = cols[4].get_text().replace(",","")
    #         if dt and dt != "\xa0":
    #             dt = float(dt)
    #         else:
    #             dt = 0
    #         ct = cols[5].get_text().replace(",","")
    #         if ct and ct != "\xa0":
    #             ct = float(ct)
    #         else:
    #             ct = 0
    #         amount = dt - ct
    #         transaction = {
    #             "date" : cols[2].get_text(),
    #             "description" : cols[1].get_text(),
    #             "vat" : cols[3].get_text(),
    #             "amount" : amount,
    #             "balance" : cols[6].get_text(),
    #         }
    #         tenant_data['Transactions'].append(transaction)
    #     data.append(tenant_data)
    # data_json = json.dumps(data, indent=1)
    # pyperclip.copy(data_json)

open_urls_in_browser(realty)