import webbrowser

tenants = [
 {
   "Tenant": "TEN00009",
   "Property": "PRO00047"
 },
 {
   "Tenant": "TEN00015",
   "Property": "PRO00051"
 },
 {
   "Tenant": "TEN00024",
   "Property": "PRO00050"
 },
 {
   "Tenant": "TEN00035",
   "Property": "PRO00053"
 },
 {
   "Tenant": "TEN00040",
   "Property": "PRO00052"
 },
 {
   "Tenant": "TEN00058",
   "Property": "PRO00307"
 },
 {
   "Tenant": "TEN00058",
   "Property": "PRO00323"
 },
 {
   "Tenant": "TEN00058",
   "Property": "PRO00338"
 },
 {
   "Tenant": "TEN00077",
   "Property": "PRO00049"
 },
 {
   "Tenant": "TEN00098",
   "Property": "PRO00317"
 },
 {
   "Tenant": "TEN00128",
   "Property": "PRO00326"
 },
 {
   "Tenant": "TEN00131",
   "Property": "PRO00304"
 },
 {
   "Tenant": "TEN00159",
   "Property": "PRO00335"
 },
 {
   "Tenant": "TEN00168",
   "Property": "PRO00334"
 },
 {
   "Tenant": "TEN00174",
   "Property": "PRO00337"
 },
 {
   "Tenant": "TEN00176",
   "Property": "PRO00339"
 },
 {
   "Tenant": "TEN00177",
   "Property": "PRO00321"
 },
 {
   "Tenant": "TEN00181",
   "Property": "PRO00330"
 },
 {
   "Tenant": "TEN00187",
   "Property": "PRO00320"
 },
 {
   "Tenant": "TEN00201",
   "Property": "PRO00315"
 },
 {
   "Tenant": "TEN00225",
   "Property": "PRO00319"
 },
 {
   "Tenant": "TEN00229",
   "Property": "PRO00046"
 },
 {
   "Tenant": "TEN00238",
   "Property": "PRO00316"
 },
 {
   "Tenant": "TEN00239",
   "Property": "PRO00336"
 },
 {
   "Tenant": "TEN00247",
   "Property": "PRO00331"
 },
 {
   "Tenant": "TEN00254",
   "Property": "PRO00312"
 },
 {
   "Tenant": "TEN00255",
   "Property": "PRO00325"
 },
 {
   "Tenant": "TEN00256",
   "Property": "PRO00311"
 },
 {
   "Tenant": "TEN00263",
   "Property": "PRO00332"
 },
 {
   "Tenant": "TEN00264",
   "Property": "PRO00329"
 },
 {
   "Tenant": "TEN00265",
   "Property": "PRO00328"
 },
 {
   "Tenant": "TEN00266",
   "Property": "PRO00338"
 },
 {
   "Tenant": "TEN00269",
   "Property": "PRO00322"
 },
 {
   "Tenant": "TEN00271",
   "Property": "PRO00314"
 },
 {
   "Tenant": "TEN00276",
   "Property": "PRO00313"
 },
 {
   "Tenant": "TEN00277",
   "Property": "PRO00310"
 },
 {
   "Tenant": "TEN00279",
   "Property": "PRO00324"
 },
 {
   "Tenant": "TEN00281",
   "Property": "PRO00309"
 },
 {
   "Tenant": "TEN00282",
   "Property": "PRO00306"
 },
 {
   "Tenant": "TEN00283",
   "Property": "PRO00318"
 },
 {
   "Tenant": "TEN00284",
   "Property": "PRO00333"
 },
 {
   "Tenant": "TEN00285",
   "Property": "PRO00327"
 },
 {
   "Tenant": "TEN00287",
   "Property": "PRO00305"
 },
 {
   "Tenant": "TEN00290",
   "Property": "PRO00308"
 },
 {
   "Tenant": "TEN00303",
   "Property": "PRO00048"
 },
 {
   "Tenant": "TEN00333",
   "Property": "PRO00045"
 },
 {
   "Tenant": "TEN00371",
   "Property": "PRO00409"
 },
 {
   "Tenant": "TEN00371",
   "Property": "PRO00441"
 },
 {
   "Tenant": "TEN00375",
   "Property": "PRO00446"
 },
 {
   "Tenant": "TEN00381",
   "Property": "PRO00454"
 },
 {
   "Tenant": "TEN00384",
   "Property": "PRO00465"
 },
 {
   "Tenant": "TEN00388",
   "Property": "PRO00313"
 },
 {
   "Tenant": "TEN00388",
   "Property": "PRO00465"
 },
 {
   "Tenant": "TEN00394",
   "Property": "PRO00313"
 },
 {
   "Tenant": "TEN00405",
   "Property": "PRO00307"
 },
 {
   "Tenant": "TEN00409",
   "Property": "PRO00338"
 },
 {
   "Tenant": "TEN00411",
   "Property": "PRO00334"
 },
 {
   "Tenant": "TEN00433",
   "Property": "PRO00316"
 },
 {
   "Tenant": "TEN00434",
   "Property": "PRO00331"
 },
 {
   "Tenant": "TEN00440",
   "Property": "PRO00309"
 },
 {
   "Tenant": "TEN00440",
   "Property": "PRO00320"
 },
 {
   "Tenant": "TEN00457",
   "Property": "PRO00307"
 },
 {
   "Tenant": "TEN00461",
   "Property": "PRO00315"
 },
 {
   "Tenant": "TEN00469",
   "Property": "PRO00337"
 },
 {
   "Tenant": "TEN00479",
   "Property": "PRO00332"
 },
 {
   "Tenant": "TEN00480",
   "Property": "PRO00323"
 },
 {
   "Tenant": "TEN00482",
   "Property": "PRO00330"
 },
 {
   "Tenant": "TEN00508",
   "Property": "PRO00317"
 },
 {
   "Tenant": "TEN00530",
   "Property": "PRO00046"
 },
 {
   "Tenant": "TEN00539",
   "Property": "PRO00323"
 },
 {
   "Tenant": "TEN00555",
   "Property": "PRO00309"
 },
 {
   "Tenant": "TEN00566",
   "Property": "PRO00319"
 },
 {
   "Tenant": "TEN00573",
   "Property": "PRO00334"
 },
 {
   "Tenant": "TEN00577",
   "Property": "PRO00315"
 },
 {
   "Tenant": "TEN00623",
   "Property": "PRO00598"
 },
 {
   "Tenant": "TEN00624",
   "Property": "PRO00446"
 },
 {
   "Tenant": "TEN00624",
   "Property": "PRO00599"
 },
 {
   "Tenant": "TEN00636",
   "Property": "PRO00333"
 },
 {
   "Tenant": "TEN00649",
   "Property": "PRO00305"
 },
 {
   "Tenant": "TEN00657",
   "Property": "PRO00330"
 },
 {
   "Tenant": "TEN00664",
   "Property": "PRO00323"
 }
]


def open_urls_in_browser(urls):
    for tenant in tenants:
        ten = tenant['Tenant']
        pro = tenant['Property']
        url = f"https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID={ten}&PID={pro}&OID=OWN00069&STD=01032022&EDD=28022023"
        webbrowser.open(url)


open_urls_in_browser(tenants)
