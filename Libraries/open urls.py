import webbrowser

tenants = [
 {
   "Property": "PRO00440",
   "FIELD2": "Anchor Pallets Income",
   "Tenant": "TEN00372",
   "FIELD4": "INCOME",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00489",
   "FIELD2": "BRENDA VILLAGE EXPENSE",
   "Tenant": "TEN00371",
   "FIELD4": "EXPENSE",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00061",
   "FIELD2": "BRENDA VILLAGE 3",
   "Tenant": "TEN00060",
   "FIELD4": "Glass View (pty) Ltd,",
   "Cell": "716722622",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00601",
   "FIELD2": "BRENDA VILLAGE UNIT 3Z",
   "Tenant": "TEN00626",
   "FIELD4": "HOY, B C",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00063",
   "FIELD2": "BRENDA VILLAGE Unit D",
   "Tenant": "TEN00088",
   "FIELD4": "JZ AUTO SERVICE AND TUNE UP CENTER (PTY) LTD",
   "Cell": "724619475",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00063",
   "FIELD2": "BRENDA VILLAGE Unit D",
   "Tenant": "TEN00702",
   "FIELD4": "MAZAMBANE TRADING 330 (PTY) LTD",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00626",
   "FIELD2": "BRENDA VILLAGE UNIT E",
   "Tenant": "TEN00614",
   "FIELD4": "GOMES, M P J",
   "Cell": "0835423753 0724605524",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00065",
   "FIELD2": "BYL TRADING (PTY) LT 19",
   "Tenant": "TEN00154",
   "FIELD4": "Mr H W Mann,",
   "Cell": "834485056",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00066",
   "FIELD2": "BYL TRADING (PTY) LT 3",
   "Tenant": "TEN00065",
   "FIELD4": "HOME OWNER ASSOCIATION (BYL 3)",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00067",
   "FIELD2": "BYL TRADING (PTY) LT 4",
   "Tenant": "TEN00016",
   "FIELD4": "MR GOUWS",
   "Cell": "724073809",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00068",
   "FIELD2": "BYL TRADING (PTY) LT 5",
   "Tenant": "TEN00351",
   "FIELD4": "TMD TOWERS (PTY) LTD",
   "Cell": "082 846 8356",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00542",
   "FIELD2": "BYL TRADING (PTY) LT 5 (SECURITY)",
   "Tenant": "TEN00351",
   "FIELD4": "TMD TOWERS (PTY) LTD",
   "Cell": "082 846 8356",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00069",
   "FIELD2": "BYL TRADING (PTY) LT 6",
   "Tenant": "TEN00116",
   "FIELD4": "MEGASURF WIRELESS INTERNET CC",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00069",
   "FIELD2": "BYL TRADING (PTY) LT 6",
   "Tenant": "TEN00351",
   "FIELD4": "TMD TOWERS (PTY) LTD",
   "Cell": "082 846 8356",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00541",
   "FIELD2": "BYL TRADING (PTY) LT 6 (SECURITY)",
   "Tenant": "TEN00116",
   "FIELD4": "MEGASURF WIRELESS INTERNET CC",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00070",
   "FIELD2": "BYL TRADING (PTY) LT 7",
   "Tenant": "TEN00363",
   "FIELD4": "Vodacom South Africa,",
   "Cell": "829974302",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00071",
   "FIELD2": "BYL TRADING (PTY) LT 8 - ARREAR ACC",
   "Tenant": "TEN00323",
   "FIELD4": "SOUTH AFRICAN POLICE SERVICES",
   "Cell": "723207542",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00545",
   "FIELD2": "BYL TRADING (PTY) LT 8 (SECURITY)",
   "Tenant": "TEN00323",
   "FIELD4": "SOUTH AFRICAN POLICE SERVICES",
   "Cell": "723207542",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00073",
   "FIELD2": "BYL TRADING (PTY) LT Stand 11",
   "Tenant": "TEN00171",
   "FIELD4": "Mr J Van Tonder,",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00532",
   "FIELD2": "BYL TRADING (PTY) LT STAND 13",
   "Tenant": "TEN00140",
   "FIELD4": "MR GW MANN",
   "Cell": "844294092",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00074",
   "FIELD2": "BYL TRADING (PTY) LT Stand 15",
   "Tenant": "TEN00167",
   "FIELD4": "MR J HATTINGH",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00075",
   "FIELD2": "BYL TRADING (PTY) LT Stand 17",
   "Tenant": "TEN00150",
   "FIELD4": "MR G W MANN",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00694",
   "FIELD2": "BYL TRADING (PTY) LT STAND 22",
   "Tenant": "TEN00801",
   "FIELD4": "VISSER, T",
   "Cell": "823720638",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00499",
   "FIELD2": "BYL TRADING (PTY) LTD 10",
   "Tenant": "TEN00417",
   "FIELD4": "LOUW BYL 10 , R",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00544",
   "FIELD2": "BYL TRADING (PTY) LTD 10 (SECURITY) Tower",
   "Tenant": "TEN00332",
   "FIELD4": "TELKOM",
   "Cell": "813539278",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00076",
   "FIELD2": "BYL TRADING (PTY) LTD 10 Tower",
   "Tenant": "TEN00332",
   "FIELD4": "TELKOM",
   "Cell": "813539278",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00500",
   "FIELD2": "BYL TRADING (PTY) LTD 12",
   "Tenant": "TEN00418",
   "FIELD4": "MANN, R",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00474",
   "FIELD2": "BYL TRADING (PTY) LTD 14",
   "Tenant": "TEN00407",
   "FIELD4": "LOMBAARD, L",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00072",
   "FIELD2": "BYL TRADING (PTY) LTD 2 Stables",
   "Tenant": "TEN00150",
   "FIELD4": "MR G W MANN",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00576",
   "FIELD2": "BYL TRADING (PTY) LTD 20",
   "Tenant": "TEN00567",
   "FIELD4": "MR G W MANN",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00523",
   "FIELD2": "BYL TRADING (PTY) LTD 23",
   "Tenant": "TEN00450",
   "FIELD4": "FOURIE, R",
   "Cell": "827718653",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00638",
   "FIELD2": "BYL TRADING (PTY) LTD 23 SERVICES",
   "Tenant": "TEN00695",
   "FIELD4": "FOURIE;MANN",
   "Cell": "827718653",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00510",
   "FIELD2": "BYL TRADING (PTY) LTD 24",
   "Tenant": "TEN00429",
   "FIELD4": "STEVENS, M",
   "Cell": "790137802",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00586",
   "FIELD2": "BYL TRADING (PTY) LTD 8",
   "Tenant": "TEN00591",
   "FIELD4": "RAS, L",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00560",
   "FIELD2": "BYL TRADING (PTY) LTD 9",
   "Tenant": "TEN00533",
   "FIELD4": "PRETORIUS, P",
   "Cell": "827523031",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00543",
   "FIELD2": "BYL TRADING (PTY) LTD 9 (SECURITY) Tower At Karma Ranch",
   "Tenant": "TEN00048",
   "FIELD4": "Eskom,",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00077",
   "FIELD2": "BYL TRADING (PTY) LTD 9 Tower At Karma Ranch",
   "Tenant": "TEN00048",
   "FIELD4": "Eskom,",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00461",
   "FIELD2": "BYL TRADING (PTY) LTD CHARLET 1",
   "Tenant": "TEN00595",
   "FIELD4": "CLAASSEN",
   "Cell": "799808181",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00461",
   "FIELD2": "BYL TRADING (PTY) LTD CHARLET 1",
   "Tenant": "TEN00385",
   "FIELD4": "NEL, L",
   "Cell": "664986692",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00064",
   "FIELD2": "BYL TRADING (PTY) LTD LODGE 1,2,3",
   "Tenant": "TEN00150",
   "FIELD4": "MR G W MANN",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00408",
   "FIELD2": "Byl Trading Expense",
   "Tenant": "TEN00371",
   "FIELD4": "EXPENSE",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00479",
   "FIELD2": "KARMA 18",
   "Tenant": "TEN00371",
   "FIELD4": "EXPENSE",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00457",
   "FIELD2": "OLIVE BRANCH EXPENSE",
   "Tenant": "TEN00371",
   "FIELD4": "EXPENSE",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00251",
   "FIELD2": "OLIVE BRANCH PARK EX1 Unit 1",
   "Tenant": "TEN00028",
   "FIELD4": "Danmik Power And Construction,",
   "Cell": "824599080",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00252",
   "FIELD2": "OLIVE BRANCH PARK EX1 Unit 4",
   "Tenant": "TEN00619",
   "FIELD4": "SUPREMECOAT HOLDINGS (PTY) LTD",
   "Cell": "829066393",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00252",
   "FIELD2": "OLIVE BRANCH PARK EX1 Unit 4",
   "Tenant": "TEN00361",
   "FIELD4": "Virlocube (pty) Ltd,",
   "Cell": "623145523",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00250",
   "FIELD2": "OLIVE BRANCH PARK EX1 Unit 5",
   "Tenant": "TEN00534",
   "FIELD4": "DANMIK POWER AND CONSTRUCTION",
   "Cell": "824599080",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00250",
   "FIELD2": "OLIVE BRANCH PARK EX1 Unit 5",
   "Tenant": "TEN00212",
   "FIELD4": "SUBTISTAR (PTY) LTD (TERM)",
   "Cell": "826037143",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00253",
   "FIELD2": "OLIVE BRANCH PARK EX1 Unit 6",
   "Tenant": "TEN00059",
   "FIELD4": "Gauglo Trading (pty) Ltd,",
   "Cell": "738419625",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00253",
   "FIELD2": "OLIVE BRANCH PARK EX1 Unit 6",
   "Tenant": "TEN00452",
   "FIELD4": "OLIWAVE PROPRIETARY LIMITED (PTY) LTD",
   "Cell": "832715885",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00604",
   "FIELD2": "OLIVE BRANCH PARK EX1 UNIT 6W",
   "Tenant": "TEN00629",
   "FIELD4": "DIG DOG (PTY) LTD",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00257",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 1",
   "Tenant": "TEN00355",
   "FIELD4": "Vaal Bag Manufactures (pty) Ltd,",
   "Cell": "605186761",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00258",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 10",
   "Tenant": "TEN00005",
   "FIELD4": "Anchor Pallets (pty) Ltd,",
   "Cell": "825362300",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00258",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 10",
   "Tenant": "TEN00605",
   "FIELD4": "CONCIV STRAT (PTY) LTD",
   "Cell": "607326797",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00692",
   "FIELD2": "OLIVE BRANCH PARK EX2 UNIT 11",
   "Tenant": "TEN00530",
   "FIELD4": "DEMOCRATIC ALLIANCE - GAUTENG",
   "Cell": "828537042",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00603",
   "FIELD2": "OLIVE BRANCH PARK EX2 UNIT 11Z",
   "Tenant": "TEN00628",
   "FIELD4": "ECONO ROOFING",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00259",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 2",
   "Tenant": "TEN00147",
   "FIELD4": "Mr G C Mileham,",
   "Cell": "786974374",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00259",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 2",
   "Tenant": "TEN00497",
   "FIELD4": "VAAL BULK BAGS (PTY) LTD",
   "Cell": "765988308",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00255",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 3",
   "Tenant": "TEN00572",
   "FIELD4": "KONECT TELECOMMUNICATIONS (PTY) LTD",
   "Cell": "813190842",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00255",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 3",
   "Tenant": "TEN00364",
   "FIELD4": "Wassmo Investments (pty) Ltd T/a Sa Fittings,",
   "Cell": "829347861",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00260",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 4",
   "Tenant": "TEN00022",
   "FIELD4": "Complete Fire Protection (pty) Ltd,",
   "Cell": "828035381",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00260",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 4",
   "Tenant": "TEN00408",
   "FIELD4": "JDS INDUSTRIES (PTY) LTD (TERM)",
   "Cell": "820477953",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00261",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 5",
   "Tenant": "TEN00072",
   "FIELD4": "JDS INDUSTRIES (PTY) LTD",
   "Cell": "820477953",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00262",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 6",
   "Tenant": "TEN00005",
   "FIELD4": "Anchor Pallets (pty) Ltd,",
   "Cell": "825362300",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00262",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 6",
   "Tenant": "TEN00437",
   "FIELD4": "THULTECH (PTY) LTD",
   "Cell": "655842865",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00263",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 7",
   "Tenant": "TEN00063",
   "FIELD4": "Hegan / Duxenro Trading,",
   "Cell": "824546797",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00264",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 8",
   "Tenant": "TEN00005",
   "FIELD4": "Anchor Pallets (pty) Ltd,",
   "Cell": "825362300",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00256",
   "FIELD2": "OLIVE BRANCH PARK EX2 Unit 9",
   "Tenant": "TEN00046",
   "FIELD4": "Dungbeetles Septic Pumping (pty) Ltd,",
   "Cell": "834440803",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00602",
   "FIELD2": "OLIVE BRANCH PARK EX2 UNIT 9Z",
   "Tenant": "TEN00627",
   "FIELD4": "T LIGHT POLE REDUCERS",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00515",
   "FIELD2": "OLIVE BRANCH PARK EX2-STORAGE SPACE UNIT 11",
   "Tenant": "TEN00436",
   "FIELD4": "ANCHOR PALLETS (PTY) LTD",
   "Cell": "825362300",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00533",
   "FIELD2": "POTCHEFSTROOM SILVER STREET 20",
   "Tenant": "TEN00666",
   "FIELD4": "GREAVER, B W",
   "Cell": "764303187",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00533",
   "FIELD2": "POTCHEFSTROOM SILVER STREET 20",
   "Tenant": "TEN00473",
   "FIELD4": "MOSHABA, A",
   "Cell": "712658664",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00590",
   "FIELD2": "SPENCE 6",
   "Tenant": "TEN00600",
   "FIELD4": "J AND M COOLING SUPPLIES (PTY) LTD",
   "Cell": "0834490984/0727278258",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00476",
   "FIELD2": "STEELE 19 (PTY) LTD 1",
   "Tenant": "TEN00150",
   "FIELD4": "MR G W MANN",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00412",
   "FIELD2": "Steele Estates EXPENSE",
   "Tenant": "TEN00371",
   "FIELD4": "EXPENSE",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00491",
   "FIELD2": "STEELE OLIVE EXT 1 EXPENSE EXPENSE",
   "Tenant": "TEN00371",
   "FIELD4": "EXPENSE",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00492",
   "FIELD2": "STEELE OLIVE EXT2 EXPENSE EXPENSE",
   "Tenant": "TEN00371",
   "FIELD4": "EXPENSE",
   "Cell": "",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00650",
   "FIELD2": "SUSPENSE ACC, VEREENIGING",
   "Tenant": "TEN00706",
   "FIELD4": "SUSPENSE ACC",
   "Cell": "",
   "Owner": "OWN00053"
 },
 {
   "Property": "PRO00596",
   "FIELD2": "THE MALL SHOP 4-ROLLER DOOR",
   "Tenant": "TEN00502",
   "FIELD4": "HI CELLULAR (PTY) LTD",
   "Cell": "624585158",
   "Owner": "OWN00079"
 },
 {
   "Property": "PRO00406",
   "FIELD2": "WESTON PARK 13",
   "Tenant": "TEN00286",
   "FIELD4": "MS R MAKHOBA",
   "Cell": "677460738",
   "Owner": "OWN00053"
 },
]


def open_urls_in_browser(urls):
    for tenant in tenants:
        ten = tenant['Tenant']
        pro = tenant['Property']
        own = tenant['Owner']
        url = f"https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID={ten}&PID={pro}&OID={own}&STD=01032022&EDD=28022023"
        webbrowser.open(url)


open_urls_in_browser(tenants)
