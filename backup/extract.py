from bs4 import BeautifulSoup
import pyperclip

# HTML content with the table
html_content = '''
<table width="100%" class="table_report" border="1">
  <tbody>
    <tr>
      <th width="160px" class="td_report" style="border-right: 0px">
        Contract Status: Active
      </th>
      <th
        width="160px"
        class="td_report"
        style="border-left: 0px; border-right: 0px"
      ></th>

      <th width="120px" colspan="6" class="td_report" style="border-left: 0px">
        Movement for (credits to oldest debt)
      </th>
    </tr>
    <tr>
      <th width="160px" class="td_report" style="border-right: 0px">
        Property
      </th>
      <th
        width="160px"
        class="td_report"
        style="border-left: 0px; border-right: 0px"
      >
        Tenant
      </th>
      <th
        width="30px"
        class="td_report"
        style="border-left: 0px; border-right: 0px"
      >
        120+ days
      </th>
      <th
        width="30px"
        class="td_report"
        style="border-left: 0px; border-right: 0px"
      >
        90 days
      </th>
      <th
        width="30px"
        class="td_report"
        style="border-left: 0px; border-right: 0px"
      >
        60 days
      </th>
      <th
        width="30px"
        class="td_report"
        style="border-left: 0px; border-right: 0px"
      >
        30 days
      </th>
      <th
        width="30px"
        class="td_report"
        style="border-left: 0px; border-right: 0px"
      >
        Current
      </th>
      <th width="30px" class="td_report" style="border-left: 0px">Total Due</th>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00718&amp;PID=PRO00658&amp;OID=OWN00193&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">10 FLAMINGO</td>
      <td class="td_report_small" style="">
        KHUMALO &amp; MASILO, G &amp; K A
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00401&amp;PID=PRO00487&amp;OID=OWN00108&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        15 KYLE CRESCENT GOLF ROAD, THREE RIVERS
      </td>
      <td class="td_report_small" style="">HEATHCOTE, J</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,820.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,820.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00655&amp;PID=PRO00504&amp;OID=OWN00116&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        16 A THEATRE STREET UNIT 1, THREE RIVERS PROPER
      </td>
      <td class="td_report_small" style="">BYLEVELDT, F</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00569&amp;PID=PRO00577&amp;OID=OWN00116&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        16 A THEATRE STREET UNIT 2
      </td>
      <td class="td_report_small" style="">KHOROMMBI, L I</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,162.98</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,162.98</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00622&amp;PID=PRO00163&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        16 JILANI HEIGHTS 16
      </td>
      <td class="td_report_small" style="">PANCHBHAYA, A Y</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,270.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,270.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00641&amp;PID=PRO00614&amp;OID=OWN00162&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        16 KARIBA BUSSINESS PARK UNIT 1
      </td>
      <td class="td_report_small" style="">FOODCORP (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">43,780.71</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">43,780.71</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00710&amp;PID=PRO00654&amp;OID=OWN00183&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        16 LA MIA CASA, THREE RIVERS
      </td>
      <td class="td_report_small" style="">OLIVEIRA, J M DC</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,953.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,953.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00673&amp;PID=PRO00622&amp;OID=OWN00169&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        2 B SPEY DRIVE UNIT -1, THREE RIVERS
      </td>
      <td class="td_report_small" style="">MBATHA, V</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">100.00</td>
      <td class="td_report_small" style="text-align: right">3,102.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,202.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00719&amp;PID=PRO00659&amp;OID=OWN00169&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        2 B SPEY DRIVE UNIT -2, THREE RIVERS
      </td>
      <td class="td_report_small" style="">MASHIGA, P L</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00676&amp;PID=PRO00625&amp;OID=OWN00169&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        2 B SPEY DRIVE UNIT -3, THREE RIVERS
      </td>
      <td class="td_report_small" style="">TSOTETSI, D G</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,750.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,750.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00674&amp;PID=PRO00623&amp;OID=OWN00169&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
      class="td_report"
    >
      <td class="td_report_small" style="border-right: 0px">
        2 B SPEY DRIVE UNIT -4, THREE RIVERS
      </td>
      <td class="td_report_small" style="">RAUTENBACH, E</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,400.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,400.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00679&amp;PID=PRO00629&amp;OID=OWN00169&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        2 B SPEY DRIVE UNIT -6, THREE RIVERS
      </td>
      <td class="td_report_small" style="">MASANGO, N</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,300.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,300.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00709&amp;PID=PRO00653&amp;OID=OWN00196&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        20 ST MITCHELL, MEYERTON CENTRAL
      </td>
      <td class="td_report_small" style="">BEYL &amp; SWART, W H F &amp; D</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">324.66</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">324.66</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00647&amp;PID=PRO00616&amp;OID=OWN00163&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        265 LOUIS TRICHARD BLVD, VANDERBIJLPARK
      </td>
      <td class="td_report_small" style="">VAAL COMPU SIGNS, P</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,920.25</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,920.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00714&amp;PID=PRO00656&amp;OID=OWN00191&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        29 ERICA STREET, ARCON PARK
      </td>
      <td class="td_report_small" style="">
        GROBLER&amp;ERASMUS, D A S &amp; H
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,300.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,300.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00720&amp;PID=PRO00660&amp;OID=OWN00194&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        3 KAROSEL STREET, THREE RIVERS
      </td>
      <td class="td_report_small" style="">BOSHOFF, A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,996.67</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,996.67</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00613&amp;PID=PRO00595&amp;OID=OWN00153&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">30 ST MITCHELL</td>
      <td class="td_report_small" style="">MHLONGO, Z N</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,600.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,600.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00537&amp;PID=PRO00561&amp;OID=OWN00137&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        31 TELFORD STREET, DUNCANVILLE
      </td>
      <td class="td_report_small" style="">SA LOADBODIE PARTS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">22,989.21</td>
      <td class="td_report_small" style="text-align: right">198,281.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">221,270.53</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00688&amp;PID=PRO00634&amp;OID=OWN00177&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        45 LETABA STREET, THREE RIVERS
      </td>
      <td class="td_report_small" style="">
        CRONJE &amp; WOODRIDGE, N M &amp; S R
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,774.46</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,774.46</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00690&amp;PID=PRO00635&amp;OID=OWN00178&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        48 CANTERBURY STREET, DUNCANVILLE
      </td>
      <td class="td_report_small" style="">VAN DEN BERGH, R</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,350.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,350.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00084&amp;PID=PRO00002&amp;OID=OWN00048&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        5 MOONDUST PROPERTIES 4
      </td>
      <td class="td_report_small" style="">
        Khp Hydraulics &amp; Pneumatics (pty) Ltd,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,196.77</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,196.77</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00726&amp;PID=PRO00663&amp;OID=OWN00195&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        6 TELFORD STREET, DUNCANVILLE
      </td>
      <td class="td_report_small" style="">
        MACSTEEL SERVICE CENTRES SA (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">100,567.50</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">100,567.50</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00659&amp;PID=PRO00605&amp;OID=OWN00156&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        60 HERBERT STREET,GOLF PARK,MEYERTON
      </td>
      <td class="td_report_small" style="">COATES, S</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,350.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,350.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00729&amp;PID=PRO00664&amp;OID=OWN00197&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        6B TAAIBOS STREET, POWERVILLE
      </td>
      <td class="td_report_small" style="">VUTHANI HOLDINGS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,406.45</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,406.45</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00678&amp;PID=PRO00628&amp;OID=OWN00171&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        70 KOOS DE LA REY, VANDERBIJLPARK CENTRAL
      </td>
      <td class="td_report_small" style="">MTNA ENGINEERING (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,800.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,800.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00700&amp;PID=PRO00642&amp;OID=OWN00184&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        73 PIET RETIEF BOULEVARD UNIT 1
      </td>
      <td class="td_report_small" style="">MUKALAY, J N</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00400&amp;PID=PRO00486&amp;OID=OWN00107&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        84 GENERAL HERTZOG UNIT 4
      </td>
      <td class="td_report_small" style="">RAMALIVHA TRADING AND PROJECTS</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">23,248.50</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">23,248.50</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00312&amp;PID=PRO00103&amp;OID=OWN00002&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        84 GENERAL HERTZOG UNIT 7
      </td>
      <td class="td_report_small" style="">
        RP COMPREHENSIVE MARKETING AGENCY CC
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,009.89</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,009.89</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00682&amp;PID=PRO00631&amp;OID=OWN00174&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        9 HEX STREET, THREE RIVERS
      </td>
      <td class="td_report_small" style="">BEKKER, J</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,600.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,600.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00240&amp;PID=PRO00005&amp;OID=OWN00029&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AKASIA FLATS 318
      </td>
      <td class="td_report_small" style="">Mr T W Ngcobo,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,342.04</td>
      <td class="td_report_small" style="text-align: right">5,603.84</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,945.88</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00117&amp;PID=PRO00006&amp;OID=OWN00060&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AKASIA FLATS 319
      </td>
      <td class="td_report_small" style="">LODAMO, A W</td>
      <td class="td_report_small" style="text-align: right">4,940.73</td>
      <td class="td_report_small" style="text-align: right">4,651.83</td>
      <td class="td_report_small" style="text-align: right">4,500.86</td>
      <td class="td_report_small" style="text-align: right">4,592.87</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,686.29</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00135&amp;PID=PRO00008&amp;OID=OWN00039&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AKASIA FLATS 417
      </td>
      <td class="td_report_small" style="">Mr A Shamisu,</td>
      <td class="td_report_small" style="text-align: right">23,970.01</td>
      <td class="td_report_small" style="text-align: right">5,159.64</td>
      <td class="td_report_small" style="text-align: right">5,167.42</td>
      <td class="td_report_small" style="text-align: right">5,333.77</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">39,630.84</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00112&amp;PID=PRO00010&amp;OID=OWN00064&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AKASIA FLATS 514
      </td>
      <td class="td_report_small" style="">Me N Sijojwana,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,778.28</td>
      <td class="td_report_small" style="text-align: right">5,403.57</td>
      <td class="td_report_small" style="text-align: right">5,564.64</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,746.49</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00606&amp;PID=PRO00495&amp;OID=OWN00111&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AKASIA FLATS 516
      </td>
      <td class="td_report_small" style="">UMALE, M R</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1.80</td>
      <td class="td_report_small" style="text-align: right">4,237.99</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,239.79</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00034&amp;PID=PRO00020&amp;OID=OWN00030&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ANDASTA BUILDING 1
      </td>
      <td class="td_report_small" style="">
        Department Of Labour &amp; Public Works,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">53,863.19</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">53,863.19</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00033&amp;PID=PRO00021&amp;OID=OWN00030&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ANDASTA BUILDING 2
      </td>
      <td class="td_report_small" style="">DEPARTMENT OF LABOUR</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">57,617.17</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">57,617.17</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00320&amp;PID=PRO00022&amp;OID=OWN00030&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ANDASTA BUILDING 3
      </td>
      <td class="td_report_small" style="">SIBIYA NN (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">11,426.65</td>
      <td class="td_report_small" style="text-align: right">6,861.09</td>
      <td class="td_report_small" style="text-align: right">6,016.21</td>
      <td class="td_report_small" style="text-align: right">6,333.83</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">30,637.78</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00061&amp;PID=PRO00023&amp;OID=OWN00030&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ANDASTA BUILDING 4
      </td>
      <td class="td_report_small" style="">GOGOME, KO</td>
      <td class="td_report_small" style="text-align: right">17,921.96</td>
      <td class="td_report_small" style="text-align: right">7,565.17</td>
      <td class="td_report_small" style="text-align: right">7,052.77</td>
      <td class="td_report_small" style="text-align: right">7,343.94</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">39,883.84</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00231&amp;PID=PRO00024&amp;OID=OWN00030&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ANDASTA BUILDING 5
      </td>
      <td class="td_report_small" style="">MR T F MAYEKISO</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">788.69</td>
      <td class="td_report_small" style="text-align: right">7,342.67</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,131.36</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00325&amp;PID=PRO00025&amp;OID=OWN00030&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ANDASTA BUILDING 6
      </td>
      <td class="td_report_small" style="">
        SOUTH AFRICAN WOMANS ACADEMY SKILLS (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">26,281.26</td>
      <td class="td_report_small" style="text-align: right">27,174.97</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">53,456.23</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00540&amp;PID=PRO00563&amp;OID=OWN00030&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ANDASTA BUILDING 7
      </td>
      <td class="td_report_small" style="">
        SOUTH AFRICAN WOMEN'S ACADEMY (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,637.14</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,637.14</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00563&amp;PID=PRO00573&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1547
      </td>
      <td class="td_report_small" style="">FERREIRA, A</td>
      <td class="td_report_small" style="text-align: right">6,877.75</td>
      <td class="td_report_small" style="text-align: right">230.28</td>
      <td class="td_report_small" style="text-align: right">295.16</td>
      <td class="td_report_small" style="text-align: right">301.06</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,704.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00717&amp;PID=PRO00549&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1548
      </td>
      <td class="td_report_small" style="">BOTHA, P F</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,999.99</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,999.99</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00614&amp;PID=PRO00597&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1549
      </td>
      <td class="td_report_small" style="">GOMES, M P J</td>
      <td class="td_report_small" style="text-align: right">23,351.01</td>
      <td class="td_report_small" style="text-align: right">12,017.02</td>
      <td class="td_report_small" style="text-align: right">12,107.36</td>
      <td class="td_report_small" style="text-align: right">12,502.51</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">59,977.90</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00423&amp;PID=PRO00505&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1551
      </td>
      <td class="td_report_small" style="">MARX, A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">522.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">522.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00576&amp;PID=PRO00570&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1552
      </td>
      <td class="td_report_small" style="">VAN SCHALKWYK, D</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,400.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,400.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00561&amp;PID=PRO00571&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1554
      </td>
      <td class="td_report_small" style="">MOKHESI, D</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,000.00</td>
      <td class="td_report_small" style="text-align: right">5,253.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,253.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00505&amp;PID=PRO00546&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1557
      </td>
      <td class="td_report_small" style="">RHANGANE, N P S</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,814.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,814.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00562&amp;PID=PRO00572&amp;OID=OWN00097&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        APEX ESTATE UNIT 1572
      </td>
      <td class="td_report_small" style="">ANNECKE, A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,250.12</td>
      <td class="td_report_small" style="text-align: right">5,178.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,428.12</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00708&amp;PID=PRO00640&amp;OID=OWN00182&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ARCON VILLAS NO 19
      </td>
      <td class="td_report_small" style="">CHIBIRA, K</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,800.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,800.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00662&amp;PID=PRO00617&amp;OID=OWN00164&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ASSEGAAI STREET 19, THREE RIVERS
      </td>
      <td class="td_report_small" style="">MATLA LIFE INVESTMENT</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,653.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,653.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00245&amp;PID=PRO00029&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 1 &amp; 5
      </td>
      <td class="td_report_small" style="">MR WP BACKEBER</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,145.86</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,145.86</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00082&amp;PID=PRO00030&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 2A
      </td>
      <td class="td_report_small" style="">KARMA 18</td>
      <td class="td_report_small" style="text-align: right">5,529.50</td>
      <td class="td_report_small" style="text-align: right">1,005.10</td>
      <td class="td_report_small" style="text-align: right">1,025.20</td>
      <td class="td_report_small" style="text-align: right">1,045.71</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,605.51</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00590&amp;PID=PRO00031&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 2B
      </td>
      <td class="td_report_small" style="">SGAMMINI, R</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,808.69</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,808.69</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00328&amp;PID=PRO00033&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 3 &amp; 6
      </td>
      <td class="td_report_small" style="">STEELE ESTATES (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">11,059.00</td>
      <td class="td_report_small" style="text-align: right">2,010.20</td>
      <td class="td_report_small" style="text-align: right">2,050.40</td>
      <td class="td_report_small" style="text-align: right">2,091.41</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,211.01</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00642&amp;PID=PRO00032&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 3
      </td>
      <td class="td_report_small" style="">WADMORE, S L</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">33.88</td>
      <td class="td_report_small" style="text-align: right">1,371.30</td>
      <td class="td_report_small" style="text-align: right">1,707.36</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,112.54</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00081&amp;PID=PRO00036&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 7A
      </td>
      <td class="td_report_small" style="">KARMA 17</td>
      <td class="td_report_small" style="text-align: right">5,529.50</td>
      <td class="td_report_small" style="text-align: right">1,005.10</td>
      <td class="td_report_small" style="text-align: right">1,025.20</td>
      <td class="td_report_small" style="text-align: right">1,045.71</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,605.51</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00173&amp;PID=PRO00037&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 7B
      </td>
      <td class="td_report_small" style="">MR JP WATKINS</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,388.15</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,388.15</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00211&amp;PID=PRO00038&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 8A
      </td>
      <td class="td_report_small" style="">MR RH GROENEWALD</td>
      <td class="td_report_small" style="text-align: right">5,529.50</td>
      <td class="td_report_small" style="text-align: right">1,005.10</td>
      <td class="td_report_small" style="text-align: right">1,025.20</td>
      <td class="td_report_small" style="text-align: right">1,045.71</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,605.51</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00257&amp;PID=PRO00039&amp;OID=OWN00006&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        AVON DRIFT BODY CORP Unit 8B
      </td>
      <td class="td_report_small" style="">Ms B Scheepers,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,412.73</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,412.73</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00589&amp;PID=PRO00040&amp;OID=OWN00007&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">AVON DRIFTS 2</td>
      <td class="td_report_small" style="">SGAMMINI, R</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00642&amp;PID=PRO00041&amp;OID=OWN00007&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">AVON DRIFTS 3</td>
      <td class="td_report_small" style="">WADMORE, S L</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00170&amp;PID=PRO00043&amp;OID=OWN00007&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">AVON DRIFTS 7</td>
      <td class="td_report_small" style="">Mr J P Watkins,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,272.88</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,272.88</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00333&amp;PID=PRO00045&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 1</td>
      <td class="td_report_small" style="">THE LOCK STOCK AND BARREL</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,000.00</td>
      <td class="td_report_small" style="text-align: right">62,973.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">70,973.32</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00530&amp;PID=PRO00046&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 2</td>
      <td class="td_report_small" style="">DEMOCRATIC ALLIANCE - GAUTENG</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,530.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,530.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00009&amp;PID=PRO00047&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 3</td>
      <td class="td_report_small" style="">BE YOU TIFUL (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,833.19</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,833.19</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00303&amp;PID=PRO00048&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 4</td>
      <td class="td_report_small" style="">PIZAZZ DANCE STUDIO</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,826.54</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,826.54</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00077&amp;PID=PRO00049&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 5</td>
      <td class="td_report_small" style="">Journey Church Sa,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,028.25</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,028.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00015&amp;PID=PRO00051&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 7</td>
      <td class="td_report_small" style="">BOWLING CLUB</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,839.25</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,839.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00040&amp;PID=PRO00052&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 8</td>
      <td class="td_report_small" style="">Downlight Trading (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">60,687.06</td>
      <td class="td_report_small" style="text-align: right">51,167.28</td>
      <td class="td_report_small" style="text-align: right">48,659.54</td>
      <td class="td_report_small" style="text-align: right">66,640.56</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">227,154.44</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00035&amp;PID=PRO00053&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">BARNYARD Unit 9</td>
      <td class="td_report_small" style="">
        DICKINSON ESTATES LETTING (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">99,077.70</td>
      <td class="td_report_small" style="text-align: right">16,211.63</td>
      <td class="td_report_small" style="text-align: right">26,958.31</td>
      <td class="td_report_small" style="text-align: right">23,096.60</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">165,344.24</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00089&amp;PID=PRO00060&amp;OID=OWN00010&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BINGLE BUILDING Shop 4
      </td>
      <td class="td_report_small" style="">
        Lazzie Auto Electrical &amp; Supreme Edge Investments ,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">45.31</td>
      <td class="td_report_small" style="text-align: right">14,957.61</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,002.92</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00060&amp;PID=PRO00061&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BRENDA VILLAGE 3
      </td>
      <td class="td_report_small" style="">Glass View (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,370.32</td>
      <td class="td_report_small" style="text-align: right">7,245.57</td>
      <td class="td_report_small" style="text-align: right">8,614.45</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">19,230.34</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00702&amp;PID=PRO00063&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BRENDA VILLAGE Unit D
      </td>
      <td class="td_report_small" style="">MAZAMBANE TRADING 330 (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">7,825.00</td>
      <td class="td_report_small" style="text-align: right">6,781.50</td>
      <td class="td_report_small" style="text-align: right">6,788.08</td>
      <td class="td_report_small" style="text-align: right">8,500.83</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">29,895.41</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00614&amp;PID=PRO00626&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BRENDA VILLAGE UNIT E
      </td>
      <td class="td_report_small" style="">GOMES, M P J</td>
      <td class="td_report_small" style="text-align: right">10,197.82</td>
      <td class="td_report_small" style="text-align: right">6,253.96</td>
      <td class="td_report_small" style="text-align: right">6,121.85</td>
      <td class="td_report_small" style="text-align: right">6,561.36</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">29,134.99</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00016&amp;PID=PRO00067&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LT 4
      </td>
      <td class="td_report_small" style="">MR GOUWS</td>
      <td class="td_report_small" style="text-align: right">21,629.33</td>
      <td class="td_report_small" style="text-align: right">867.43</td>
      <td class="td_report_small" style="text-align: right">520.22</td>
      <td class="td_report_small" style="text-align: right">530.62</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">23,547.60</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00351&amp;PID=PRO00542&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LT 5 (SECURITY)
      </td>
      <td class="td_report_small" style="">TMD TOWERS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">3,002.28</td>
      <td class="td_report_small" style="text-align: right">1,500.00</td>
      <td class="td_report_small" style="text-align: right">1,500.00</td>
      <td class="td_report_small" style="text-align: right">1,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,502.28</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00351&amp;PID=PRO00069&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LT 6
      </td>
      <td class="td_report_small" style="">TMD TOWERS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,812.50</td>
      <td class="td_report_small" style="text-align: right">4,312.50</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,125.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00323&amp;PID=PRO00071&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LT 8 - ARREAR ACC
      </td>
      <td class="td_report_small" style="">SOUTH AFRICAN POLICE SERVICES</td>
      <td class="td_report_small" style="text-align: right">394,686.11</td>
      <td class="td_report_small" style="text-align: right">16,893.72</td>
      <td class="td_report_small" style="text-align: right">17,231.60</td>
      <td class="td_report_small" style="text-align: right">17,576.23</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">446,387.66</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00323&amp;PID=PRO00545&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LT 8 (SECURITY)
      </td>
      <td class="td_report_small" style="">SOUTH AFRICAN POLICE SERVICES</td>
      <td class="td_report_small" style="text-align: right">46,163.14</td>
      <td class="td_report_small" style="text-align: right">3,000.00</td>
      <td class="td_report_small" style="text-align: right">3,983.26</td>
      <td class="td_report_small" style="text-align: right">4,062.93</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">57,209.33</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00150&amp;PID=PRO00075&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LT Stand 17
      </td>
      <td class="td_report_small" style="">MR G W MANN</td>
      <td class="td_report_small" style="text-align: right">12,264.21</td>
      <td class="td_report_small" style="text-align: right">3,497.85</td>
      <td class="td_report_small" style="text-align: right">5,073.48</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">20,835.54</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00332&amp;PID=PRO00544&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LTD 10 (SECURITY) Tower
      </td>
      <td class="td_report_small" style="">TELKOM</td>
      <td class="td_report_small" style="text-align: right">42,000.00</td>
      <td class="td_report_small" style="text-align: right">3,000.00</td>
      <td class="td_report_small" style="text-align: right">3,000.00</td>
      <td class="td_report_small" style="text-align: right">3,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">51,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00418&amp;PID=PRO00500&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LTD 12
      </td>
      <td class="td_report_small" style="">MANN, R</td>
      <td class="td_report_small" style="text-align: right">1,547.14</td>
      <td class="td_report_small" style="text-align: right">735.83</td>
      <td class="td_report_small" style="text-align: right">1,674.28</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,957.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00150&amp;PID=PRO00072&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LTD 2 Stables
      </td>
      <td class="td_report_small" style="">MR G W MANN</td>
      <td class="td_report_small" style="text-align: right">12,975.53</td>
      <td class="td_report_small" style="text-align: right">2,799.35</td>
      <td class="td_report_small" style="text-align: right">8,278.07</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">24,052.95</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00695&amp;PID=PRO00638&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LTD 23 SERVICES
      </td>
      <td class="td_report_small" style="">FOURIE;MANN</td>
      <td class="td_report_small" style="text-align: right">1,130,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,130,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00048&amp;PID=PRO00543&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LTD 9 (SECURITY) Tower At Karma Ranch
      </td>
      <td class="td_report_small" style="">Eskom,</td>
      <td class="td_report_small" style="text-align: right">46,514.62</td>
      <td class="td_report_small" style="text-align: right">3,000.00</td>
      <td class="td_report_small" style="text-align: right">3,990.29</td>
      <td class="td_report_small" style="text-align: right">4,070.10</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">57,575.01</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00595&amp;PID=PRO00461&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        BYL TRADING (PTY) LTD CHARLET 1
      </td>
      <td class="td_report_small" style="">CLAASSEN</td>
      <td class="td_report_small" style="text-align: right">19,532.76</td>
      <td class="td_report_small" style="text-align: right">4,580.66</td>
      <td class="td_report_small" style="text-align: right">4,482.27</td>
      <td class="td_report_small" style="text-align: right">4,724.91</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">33,320.60</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00701&amp;PID=PRO00643&amp;OID=OWN00180&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">CALITZ COURT 11</td>
      <td class="td_report_small" style="">MAKAPELA, V M</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,700.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,700.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00694&amp;PID=PRO00637&amp;OID=OWN00180&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">CALITZ COURT 1</td>
      <td class="td_report_small" style="">SIBISI, N N</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,700.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,700.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00724&amp;PID=PRO00662&amp;OID=OWN00180&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">CALITZ COURT 3</td>
      <td class="td_report_small" style="">HADEBE, S M C</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00722&amp;PID=PRO00661&amp;OID=OWN00180&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">CALITZ COURT 7</td>
      <td class="td_report_small" style="">BUTHELEZI, B</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,130.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,130.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00378&amp;PID=PRO00448&amp;OID=OWN00031&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        COPPER SUNSET TRADING UNIT 3
      </td>
      <td class="td_report_small" style="">SIBUSISIWE CONSULTING</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,331.46</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,331.46</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00380&amp;PID=PRO00449&amp;OID=OWN00031&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        COPPER SUNSET TRADING UNIT 4
      </td>
      <td class="td_report_small" style="">MOGLEG SHEQ</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,938.35</td>
      <td class="td_report_small" style="text-align: right">2,352.52</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,290.87</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00635&amp;PID=PRO00609&amp;OID=OWN00158&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">DEMADA 204</td>
      <td class="td_report_small" style="">MOTSAU, K O</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,416.76</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,416.76</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00037&amp;PID=PRO00084&amp;OID=OWN00085&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ELIGWA ESTATE 1078
      </td>
      <td class="td_report_small" style="">Dig Dog (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,374.08</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,374.08</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00124&amp;PID=PRO00085&amp;OID=OWN00052&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ELIGWA ESTATES 1077
      </td>
      <td class="td_report_small" style="">
        Mr &amp; Mrs D &amp; K De Villiers,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,725.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,725.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00426&amp;PID=PRO00086&amp;OID=OWN00054&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ELIGWA ESTATES 1087
      </td>
      <td class="td_report_small" style="">LOUW, R</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00142&amp;PID=PRO00087&amp;OID=OWN00085&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ELIGWA ESTATES 1090
      </td>
      <td class="td_report_small" style="">Mr D Schutte,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,621.67</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,621.67</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00612&amp;PID=PRO00594&amp;OID=OWN00152&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ELIGWA ESTATES 1105
      </td>
      <td class="td_report_small" style="">ORR, W C</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00501&amp;PID=PRO00088&amp;OID=OWN00009&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ELIGWA ESTATES 1143
      </td>
      <td class="td_report_small" style="">RIEDER, J A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,537.62</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,537.62</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00222&amp;PID=PRO00089&amp;OID=OWN00054&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ELIGWA ESTATES 1153
      </td>
      <td class="td_report_small" style="">MR S MAPHALALA</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,559.09</td>
      <td class="td_report_small" style="text-align: right">15,002.51</td>
      <td class="td_report_small" style="text-align: right">17,945.56</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">45,507.16</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00350&amp;PID=PRO00090&amp;OID=OWN00022&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        ERF 286 (PTY) LTD 1
      </td>
      <td class="td_report_small" style="">
        THE UNIVERSAL CHURCH OF THE KINGDOM OF GOD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,719.99</td>
      <td class="td_report_small" style="text-align: right">44,291.05</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">54,011.04</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00693&amp;PID=PRO00463&amp;OID=OWN00025&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GCJ PROPERTIES SHOP 1
      </td>
      <td class="td_report_small" style="">DANS AUTO CLINIC (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,575.00</td>
      <td class="td_report_small" style="text-align: right">10,711.50</td>
      <td class="td_report_small" style="text-align: right">11,231.73</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">37,518.23</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00360&amp;PID=PRO00100&amp;OID=OWN00025&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GCJ PROPERTIES Shop 2
      </td>
      <td class="td_report_small" style="">
        Vicshumas Panel Beaters And Spray Painting,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,514.53</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,514.53</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00076&amp;PID=PRO00101&amp;OID=OWN00025&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GCJ PROPERTIES Shop 3
      </td>
      <td class="td_report_small" style="">Joshua Trading Projects,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,806.28</td>
      <td class="td_report_small" style="text-align: right">13,998.79</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,805.07</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00652&amp;PID=PRO00102&amp;OID=OWN00025&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GCJ PROPERTIES Shop 4
      </td>
      <td class="td_report_small" style="">
        MUSCLE AUTOMOTIVE ENGINEERING (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,536.89</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,536.89</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00301&amp;PID=PRO00107&amp;OID=OWN00070&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GOLDEN SUN COURT 1
      </td>
      <td class="td_report_small" style="">PICK N PAY RETAILERS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">10,666.08</td>
      <td class="td_report_small" style="text-align: right">174,862.38</td>
      <td class="td_report_small" style="text-align: right">177,181.63</td>
      <td class="td_report_small" style="text-align: right">76,157.23</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">438,867.32</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00012&amp;PID=PRO00114&amp;OID=OWN00070&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GOLDEN SUN COURT Shop 1
      </td>
      <td class="td_report_small" style="">BIG TIME TAVERN (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,362.60</td>
      <td class="td_report_small" style="text-align: right">18,875.90</td>
      <td class="td_report_small" style="text-align: right">30,554.68</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">62,793.18</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00030&amp;PID=PRO00115&amp;OID=OWN00070&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GOLDEN SUN COURT Shop 2
      </td>
      <td class="td_report_small" style="">DC TAKE AWAY</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.43</td>
      <td class="td_report_small" style="text-align: right">19,328.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">19,328.75</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00329&amp;PID=PRO00118&amp;OID=OWN00026&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        GOODYEAR BUILDING Unit 2
      </td>
      <td class="td_report_small" style="">VAAL STUDENT HOUSING (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">110,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">110,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00190&amp;PID=PRO00125&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        HERTZOG FLATS 12
      </td>
      <td class="td_report_small" style="">Mr M Mtimkulu,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,900.92</td>
      <td class="td_report_small" style="text-align: right">6,056.91</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,957.83</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00445&amp;PID=PRO00123&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 1</td>
      <td class="td_report_small" style="">NDABA, T P</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,180.89</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,180.89</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00241&amp;PID=PRO00126&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 2</td>
      <td class="td_report_small" style="">MR T.D GEMEBA</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,071.73</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,071.73</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00246&amp;PID=PRO00127&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 3</td>
      <td class="td_report_small" style="">Mr X J Ngobese,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,577.51</td>
      <td class="td_report_small" style="text-align: right">4,584.58</td>
      <td class="td_report_small" style="text-align: right">4,773.94</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,936.03</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00232&amp;PID=PRO00128&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 4</td>
      <td class="td_report_small" style="">Mr T G Buthelezi,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,677.12</td>
      <td class="td_report_small" style="text-align: right">4,648.46</td>
      <td class="td_report_small" style="text-align: right">4,839.10</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,164.68</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00119&amp;PID=PRO00129&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 5</td>
      <td class="td_report_small" style="">MISS H C MEY</td>
      <td class="td_report_small" style="text-align: right">21,671.52</td>
      <td class="td_report_small" style="text-align: right">4,011.90</td>
      <td class="td_report_small" style="text-align: right">3,962.60</td>
      <td class="td_report_small" style="text-align: right">4,239.52</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">33,885.54</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00186&amp;PID=PRO00130&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 6</td>
      <td class="td_report_small" style="">MR M A MTIMKULU</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,339.43</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,339.43</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00513&amp;PID=PRO00131&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 7</td>
      <td class="td_report_small" style="">LAMBEBO, E D</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">136.60</td>
      <td class="td_report_small" style="text-align: right">4,746.22</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,882.82</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00241&amp;PID=PRO00551&amp;OID=OWN00023&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">HERTZOG FLATS 9</td>
      <td class="td_report_small" style="">MR T.D GEMEBA</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,101.07</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,101.07</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00696&amp;PID=PRO00639&amp;OID=OWN00181&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 11</td>
      <td class="td_report_small" style="">STEINBERG, E M</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00109&amp;PID=PRO00133&amp;OID=OWN00056&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 12</td>
      <td class="td_report_small" style="">Me K A Moroe,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,979.28</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,979.28</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00460&amp;PID=PRO00528&amp;OID=OWN00119&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 13</td>
      <td class="td_report_small" style="">KHUMALO, N M</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,620.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,620.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00670&amp;PID=PRO00621&amp;OID=OWN00119&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 15</td>
      <td class="td_report_small" style="">HLAPANE, R T</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,800.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,800.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00644&amp;PID=PRO00513&amp;OID=OWN00119&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 17</td>
      <td class="td_report_small" style="">JANSEN, Z</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,500.00</td>
      <td class="td_report_small" style="text-align: right">4,590.00</td>
      <td class="td_report_small" style="text-align: right">4,834.80</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,924.80</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00001&amp;PID=PRO00134&amp;OID=OWN00056&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 18</td>
      <td class="td_report_small" style="">ACTOP ASPHALT (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00721&amp;PID=PRO00636&amp;OID=OWN00179&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 5</td>
      <td class="td_report_small" style="">SINGH, N</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,300.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,300.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00314&amp;PID=PRO00135&amp;OID=OWN00056&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 7</td>
      <td class="td_report_small" style="">Ruu Logistics (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,253.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,253.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00492&amp;PID=PRO00517&amp;OID=OWN00120&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">INES PLACE 9</td>
      <td class="td_report_small" style="">ZONDI, N S</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,026.55</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,026.55</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00275&amp;PID=PRO00137&amp;OID=OWN00033&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">IVY STREET 21</td>
      <td class="td_report_small" style="">MS N D KRUGER</td>
      <td class="td_report_small" style="text-align: right">12,539.03</td>
      <td class="td_report_small" style="text-align: right">8,690.20</td>
      <td class="td_report_small" style="text-align: right">8,496.44</td>
      <td class="td_report_small" style="text-align: right">7,955.51</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">37,681.18</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00367&amp;PID=PRO00138&amp;OID=OWN00034&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JESSOP BUILDING Shop 2
      </td>
      <td class="td_report_small" style="">Wicker Wonder Weaver (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00137&amp;PID=PRO00140&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 10</td>
      <td class="td_report_small" style="">Mr Amed Mahmud Patel,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12.50</td>
      <td class="td_report_small" style="text-align: right">5,154.56</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,167.06</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00182&amp;PID=PRO00141&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 12</td>
      <td class="td_report_small" style="">MR L MUSLIM</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,420.60</td>
      <td class="td_report_small" style="text-align: right">5,478.28</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,898.88</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00223&amp;PID=PRO00142&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 13</td>
      <td class="td_report_small" style="">MANTI, M</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,154.31</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,154.31</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00552&amp;PID=PRO00143&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 14</td>
      <td class="td_report_small" style="">SHAHEBO, G O</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">978.35</td>
      <td class="td_report_small" style="text-align: right">5,472.59</td>
      <td class="td_report_small" style="text-align: right">5,632.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,083.26</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00715&amp;PID=PRO00144&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 16</td>
      <td class="td_report_small" style="">SHAIKH, Y H</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,670.00</td>
      <td class="td_report_small" style="text-align: right">5,409.40</td>
      <td class="td_report_small" style="text-align: right">5,564.59</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,643.99</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00640&amp;PID=PRO00613&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 17</td>
      <td class="td_report_small" style="">BELIM, A A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,107.02</td>
      <td class="td_report_small" style="text-align: right">5,395.14</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,502.16</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00216&amp;PID=PRO00145&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 18</td>
      <td class="td_report_small" style="">Mr S H Patel,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,975.81</td>
      <td class="td_report_small" style="text-align: right">5,314.96</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,290.77</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00546&amp;PID=PRO00564&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 19</td>
      <td class="td_report_small" style="">MASOUD, I S N</td>
      <td class="td_report_small" style="text-align: right">5,436.71</td>
      <td class="td_report_small" style="text-align: right">5,632.73</td>
      <td class="td_report_small" style="text-align: right">5,595.39</td>
      <td class="td_report_small" style="text-align: right">5,756.30</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">22,421.13</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00526&amp;PID=PRO00139&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 1</td>
      <td class="td_report_small" style="">SAMISO, F M</td>
      <td class="td_report_small" style="text-align: right">4,943.32</td>
      <td class="td_report_small" style="text-align: right">6,233.87</td>
      <td class="td_report_small" style="text-align: right">5,557.95</td>
      <td class="td_report_small" style="text-align: right">5,957.70</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">22,692.84</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00220&amp;PID=PRO00147&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 20</td>
      <td class="td_report_small" style="">Mr S M Desai,</td>
      <td class="td_report_small" style="text-align: right">26,477.77</td>
      <td class="td_report_small" style="text-align: right">6,161.17</td>
      <td class="td_report_small" style="text-align: right">5,911.93</td>
      <td class="td_report_small" style="text-align: right">6,006.46</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">44,557.33</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00559&amp;PID=PRO00148&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 21</td>
      <td class="td_report_small" style="">HASSAN, H</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">259.24</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">259.24</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00136&amp;PID=PRO00149&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 22</td>
      <td class="td_report_small" style="">Mr A Sherbhai,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">772.99</td>
      <td class="td_report_small" style="text-align: right">5,097.90</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,870.89</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00467&amp;PID=PRO00472&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 24</td>
      <td class="td_report_small" style="">BANDA, K L</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,082.44</td>
      <td class="td_report_small" style="text-align: right">5,337.09</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,419.53</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00594&amp;PID=PRO00146&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 2</td>
      <td class="td_report_small" style="">SHAH, M I</td>
      <td class="td_report_small" style="text-align: right">800.01</td>
      <td class="td_report_small" style="text-align: right">5,896.00</td>
      <td class="td_report_small" style="text-align: right">5,403.92</td>
      <td class="td_report_small" style="text-align: right">5,665.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,764.93</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00397&amp;PID=PRO00151&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 3</td>
      <td class="td_report_small" style="">BADAT, Z Y</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,300.25</td>
      <td class="td_report_small" style="text-align: right">5,405.20</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,705.45</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00402&amp;PID=PRO00152&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 4</td>
      <td class="td_report_small" style="">ALI, A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">47.61</td>
      <td class="td_report_small" style="text-align: right">5,547.22</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,594.83</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00427&amp;PID=PRO00153&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 5</td>
      <td class="td_report_small" style="">MOTALA, A M</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">181.57</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">181.57</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00161&amp;PID=PRO00154&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 6</td>
      <td class="td_report_small" style="">KARWA, S Y</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">54.90</td>
      <td class="td_report_small" style="text-align: right">5,486.29</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,541.19</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00531&amp;PID=PRO00155&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 7</td>
      <td class="td_report_small" style="">DESAI, M F S</td>
      <td class="td_report_small" style="text-align: right">38,056.56</td>
      <td class="td_report_small" style="text-align: right">6,397.32</td>
      <td class="td_report_small" style="text-align: right">6,595.78</td>
      <td class="td_report_small" style="text-align: right">6,592.96</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">57,642.62</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00189&amp;PID=PRO00156&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 8</td>
      <td class="td_report_small" style="">BADAT</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,827.50</td>
      <td class="td_report_small" style="text-align: right">7,671.46</td>
      <td class="td_report_small" style="text-align: right">6,337.89</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,836.85</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00553&amp;PID=PRO00568&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JILANI COURT 9</td>
      <td class="td_report_small" style="">BHAIYAT, M I</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,771.90</td>
      <td class="td_report_small" style="text-align: right">5,562.44</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,334.34</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00681&amp;PID=PRO00567&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 23
      </td>
      <td class="td_report_small" style="">BANVA, A A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,100.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,100.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00646&amp;PID=PRO00172&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 24
      </td>
      <td class="td_report_small" style="">MOHAMMAD, N</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,045.60</td>
      <td class="td_report_small" style="text-align: right">5,120.91</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,166.51</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00127&amp;PID=PRO00158&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 10
      </td>
      <td class="td_report_small" style="">Mr A Aiyub,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">91.93</td>
      <td class="td_report_small" style="text-align: right">5,656.15</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,748.08</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00198&amp;PID=PRO00159&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 11
      </td>
      <td class="td_report_small" style="">Mr M Y Sujee,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,154.24</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,154.24</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00425&amp;PID=PRO00508&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 12
      </td>
      <td class="td_report_small" style="">NAICKER, C T</td>
      <td class="td_report_small" style="text-align: right">2,499.80</td>
      <td class="td_report_small" style="text-align: right">5,787.00</td>
      <td class="td_report_small" style="text-align: right">4,818.74</td>
      <td class="td_report_small" style="text-align: right">5,674.11</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,779.65</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00653&amp;PID=PRO00160&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 13
      </td>
      <td class="td_report_small" style="">JANGDA, I A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,518.31</td>
      <td class="td_report_small" style="text-align: right">5,323.37</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,841.68</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00630&amp;PID=PRO00161&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 14
      </td>
      <td class="td_report_small" style="">PANCHBHAYA, P A Y</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,099.86</td>
      <td class="td_report_small" style="text-align: right">5,270.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,369.86</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00403&amp;PID=PRO00162&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 15
      </td>
      <td class="td_report_small" style="">MAWLALEE, M</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,656.46</td>
      <td class="td_report_small" style="text-align: right">5,588.13</td>
      <td class="td_report_small" style="text-align: right">5,722.89</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">16,967.48</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00195&amp;PID=PRO00164&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 17
      </td>
      <td class="td_report_small" style="">EBRAHIM</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,665.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,665.32</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00166&amp;PID=PRO00169&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 18 NEW
      </td>
      <td class="td_report_small" style="">Mr J H Banva,</td>
      <td class="td_report_small" style="text-align: right">46,044.81</td>
      <td class="td_report_small" style="text-align: right">6,325.21</td>
      <td class="td_report_small" style="text-align: right">6,301.71</td>
      <td class="td_report_small" style="text-align: right">6,480.74</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">65,152.47</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00206&amp;PID=PRO00166&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 19
      </td>
      <td class="td_report_small" style="">Mr P Reddy,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,822.89</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,822.89</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00163&amp;PID=PRO00157&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 1
      </td>
      <td class="td_report_small" style="">MR IMRAN AHMED JOGIAT</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,225.95</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,225.95</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00669&amp;PID=PRO00168&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 20
      </td>
      <td class="td_report_small" style="">VISKARMA, M A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,019.00</td>
      <td class="td_report_small" style="text-align: right">5,292.38</td>
      <td class="td_report_small" style="text-align: right">5,439.23</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,750.61</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00478&amp;PID=PRO00165&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 21
      </td>
      <td class="td_report_small" style="">MULLA, S M R</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,568.29</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,568.29</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00134&amp;PID=PRO00170&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 22
      </td>
      <td class="td_report_small" style="">MR A MALLA</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">161.22</td>
      <td class="td_report_small" style="text-align: right">5,282.66</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,443.88</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00645&amp;PID=PRO00173&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 25
      </td>
      <td class="td_report_small" style="">BANVA, S I</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,100.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,100.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00672&amp;PID=PRO00174&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 26
      </td>
      <td class="td_report_small" style="">ERISSO, M L</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,452.12</td>
      <td class="td_report_small" style="text-align: right">5,515.54</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,967.66</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00527&amp;PID=PRO00175&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 27
      </td>
      <td class="td_report_small" style="">ELSEBO, M D</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,902.05</td>
      <td class="td_report_small" style="text-align: right">5,418.48</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,320.53</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00194&amp;PID=PRO00167&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 2
      </td>
      <td class="td_report_small" style="">Mr M R Islam,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,352.67</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,352.67</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00217&amp;PID=PRO00176&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 3
      </td>
      <td class="td_report_small" style="">Mr S I Norat,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,226.19</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,226.19</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00197&amp;PID=PRO00177&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 4
      </td>
      <td class="td_report_small" style="">Mr M S Jangda,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,200.55</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,200.55</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00156&amp;PID=PRO00178&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 5
      </td>
      <td class="td_report_small" style="">MR I HANSROD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,216.79</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,216.79</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00200&amp;PID=PRO00179&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 6
      </td>
      <td class="td_report_small" style="">Mr N S Ismail,</td>
      <td class="td_report_small" style="text-align: right">171,416.54</td>
      <td class="td_report_small" style="text-align: right">9,028.52</td>
      <td class="td_report_small" style="text-align: right">8,939.09</td>
      <td class="td_report_small" style="text-align: right">9,166.87</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">198,551.02</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00200&amp;PID=PRO00180&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 7
      </td>
      <td class="td_report_small" style="">Mr N S Ismail,</td>
      <td class="td_report_small" style="text-align: right">212,020.92</td>
      <td class="td_report_small" style="text-align: right">9,840.61</td>
      <td class="td_report_small" style="text-align: right">9,767.42</td>
      <td class="td_report_small" style="text-align: right">10,011.77</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">241,640.72</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00549&amp;PID=PRO00181&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 8
      </td>
      <td class="td_report_small" style="">PATEL, S</td>
      <td class="td_report_small" style="text-align: right">6,643.41</td>
      <td class="td_report_small" style="text-align: right">6,054.92</td>
      <td class="td_report_small" style="text-align: right">5,684.16</td>
      <td class="td_report_small" style="text-align: right">5,907.49</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">24,289.98</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00228&amp;PID=PRO00182&amp;OID=OWN00037&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        JILANI HEIGHTS 9
      </td>
      <td class="td_report_small" style="">MR S Y KHANJI</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">76.46</td>
      <td class="td_report_small" style="text-align: right">5,098.99</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,175.45</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00289&amp;PID=PRO00183&amp;OID=OWN00068&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">JULIAN STREET 5</td>
      <td class="td_report_small" style="">MS V P NDLEBE</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00578&amp;PID=PRO00578&amp;OID=OWN00142&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KEISKAMMA 77</td>
      <td class="td_report_small" style="">VAN DEN BERG, G</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">190.24</td>
      <td class="td_report_small" style="text-align: right">11,003.80</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,194.04</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00353&amp;PID=PRO00184&amp;OID=OWN00077&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KING PARK BUILDING 7
      </td>
      <td class="td_report_small" style="">UNITED BEARINGS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,898.41</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,898.41</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00023&amp;PID=PRO00186&amp;OID=OWN00077&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KING PARK BUILDING Shop 1 &amp; 2
      </td>
      <td class="td_report_small" style="">
        Corky's Services &amp; Repairs C.c,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,066.57</td>
      <td class="td_report_small" style="text-align: right">17,353.76</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">21,420.33</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00069&amp;PID=PRO00185&amp;OID=OWN00077&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KING PARK BUILDING Shop 5
      </td>
      <td class="td_report_small" style="">INK STREET GRAPHICS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">225.38</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">225.38</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00692&amp;PID=PRO00187&amp;OID=OWN00077&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KING PARK BUILDING Shop 8
      </td>
      <td class="td_report_small" style="">
        RAINBOW DELIVERY SOLUTIONS (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,998.92</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,998.92</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00603&amp;PID=PRO00188&amp;OID=OWN00077&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KING PARK BUILDING Unit 6
      </td>
      <td class="td_report_small" style="">PRISTENE CHEMICALS</td>
      <td class="td_report_small" style="text-align: right">3,882.50</td>
      <td class="td_report_small" style="text-align: right">4,914.69</td>
      <td class="td_report_small" style="text-align: right">4,480.41</td>
      <td class="td_report_small" style="text-align: right">1,176.23</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,453.83</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00152&amp;PID=PRO00192&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KLIPHUIS 10</td>
      <td class="td_report_small" style="">Mr H J De Beer,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,507.87</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,507.87</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00102&amp;PID=PRO00195&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KLIPHUIS 13</td>
      <td class="td_report_small" style="">Me A Gouws,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,926.47</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,926.47</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00165&amp;PID=PRO00196&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KLIPHUIS 14</td>
      <td class="td_report_small" style="">MR J G VAN DER BERG</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,930.90</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,930.90</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00172&amp;PID=PRO00197&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KLIPHUIS 15</td>
      <td class="td_report_small" style="">MR JC DU PREEZ</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,930.90</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,930.90</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00202&amp;PID=PRO00198&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KLIPHUIS 16</td>
      <td class="td_report_small" style="">MR P A M VAN DER BERG</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,930.90</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,930.90</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00133&amp;PID=PRO00199&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KLIPHUIS 18</td>
      <td class="td_report_small" style="">Mr A M C Carrega,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,872.20</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,872.20</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00019&amp;PID=PRO00200&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KLIPPLAATDRIFT COMME 1
      </td>
      <td class="td_report_small" style="">Cell C,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,208.89</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,208.89</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00298&amp;PID=PRO00201&amp;OID=OWN00041&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KLIPPLAATDRIFT COMME Unit 2
      </td>
      <td class="td_report_small" style="">PANDOBUZZ (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">28,515.25</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">28,515.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00671&amp;PID=PRO00592&amp;OID=OWN00151&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KOOS DE LA REY NO 39 UNIT 1
      </td>
      <td class="td_report_small" style="">MASALA, M</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,499.71</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,499.71</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00632&amp;PID=PRO00606&amp;OID=OWN00151&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KOOS DE LA REY NO 39 UNIT 2
      </td>
      <td class="td_report_small" style="">NTIKANG, K K</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,350.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,350.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00374&amp;PID=PRO00445&amp;OID=OWN00033&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        KOWIE 20, THREE RIVERS
      </td>
      <td class="td_report_small" style="">GROENEWALD, E T</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,748.05</td>
      <td class="td_report_small" style="text-align: right">7,812.46</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,560.51</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00078&amp;PID=PRO00202&amp;OID=OWN00046&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KOWIE STREET 54</td>
      <td class="td_report_small" style="">JUDITH DOROTHY J D GOUDEN</td>
      <td class="td_report_small" style="text-align: right">11,149.34</td>
      <td class="td_report_small" style="text-align: right">5,428.50</td>
      <td class="td_report_small" style="text-align: right">5,428.50</td>
      <td class="td_report_small" style="text-align: right">5,428.50</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">27,434.84</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00633&amp;PID=PRO00607&amp;OID=OWN00157&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">KRONEDAL 101</td>
      <td class="td_report_small" style="">MADLALA, T J</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">915.55</td>
      <td class="td_report_small" style="text-align: right">5,628.31</td>
      <td class="td_report_small" style="text-align: right">5,783.88</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,327.74</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00638&amp;PID=PRO00611&amp;OID=OWN00159&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">LANCOVE NO 7</td>
      <td class="td_report_small" style="">VISSER(HORVATH), L S</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00668&amp;PID=PRO00620&amp;OID=OWN00167&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        LEE AVENUE 27 ARCON VILLAS, ARCON PARK
      </td>
      <td class="td_report_small" style="">MANN HOLDINGS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,000.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,000.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00184&amp;PID=PRO00203&amp;OID=OWN00076&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        LETABA STREET 39
      </td>
      <td class="td_report_small" style="">Mr L T H Enslin,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,923.93</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,923.93</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00371&amp;PID=PRO00436&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        Majore Building Expense
      </td>
      <td class="td_report_small" style="">EXPENSE</td>
      <td class="td_report_small" style="text-align: right">620.76</td>
      <td class="td_report_small" style="text-align: right">12.42</td>
      <td class="td_report_small" style="text-align: right">12.66</td>
      <td class="td_report_small" style="text-align: right">12.92</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">658.76</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00064&amp;PID=PRO00208&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAJORE BUILDING Shop 10
      </td>
      <td class="td_report_small" style="">Hennies Auto Electrical,</td>
      <td class="td_report_small" style="text-align: right">34,753.17</td>
      <td class="td_report_small" style="text-align: right">11,395.53</td>
      <td class="td_report_small" style="text-align: right">9,766.58</td>
      <td class="td_report_small" style="text-align: right">8,451.90</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">64,367.18</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00057&amp;PID=PRO00210&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAJORE BUILDING Shop 1
      </td>
      <td class="td_report_small" style="">FRONT LINE AUTO PARTS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">138,887.98</td>
      <td class="td_report_small" style="text-align: right">16,118.11</td>
      <td class="td_report_small" style="text-align: right">16,531.57</td>
      <td class="td_report_small" style="text-align: right">16,789.31</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">188,326.97</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00557&amp;PID=PRO00209&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAJORE BUILDING Shop 2
      </td>
      <td class="td_report_small" style="">CUTWOOD PROJECTS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,586.77</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,586.77</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00210&amp;PID=PRO00211&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAJORE BUILDING Shop 4
      </td>
      <td class="td_report_small" style="">Mr R J Seatla,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,821.98</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,821.98</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00571&amp;PID=PRO00213&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAJORE BUILDING Shop 6
      </td>
      <td class="td_report_small" style="">KOPANENG ARMOUR (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,684.42</td>
      <td class="td_report_small" style="text-align: right">6,448.44</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,132.86</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00465&amp;PID=PRO00530&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAJORE BUILDING SHOP 9
      </td>
      <td class="td_report_small" style="">MULLER, J</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.69</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.69</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00162&amp;PID=PRO00215&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAKRIEKIE MELKERY 2
      </td>
      <td class="td_report_small" style="">Mr I Shahzad,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,430.97</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,430.97</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00074&amp;PID=PRO00216&amp;OID=OWN00045&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MAKRIEKIE MELKERY Shop 1
      </td>
      <td class="td_report_small" style="">Jjj Scrap Metals,</td>
      <td class="td_report_small" style="text-align: right">33,712.64</td>
      <td class="td_report_small" style="text-align: right">4,751.28</td>
      <td class="td_report_small" style="text-align: right">4,329.94</td>
      <td class="td_report_small" style="text-align: right">4,744.54</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">47,538.40</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00356&amp;PID=PRO00218&amp;OID=OWN00015&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MATUS BUILDING 4
      </td>
      <td class="td_report_small" style="">
        VAAL TRIANGLE TOMBSTONES (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,112.83</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,112.83</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00319&amp;PID=PRO00219&amp;OID=OWN00015&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MATUS BUILDING Shop 1
      </td>
      <td class="td_report_small" style="">SHARP HARDWARE CC</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">35,950.14</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">35,950.14</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00205&amp;PID=PRO00220&amp;OID=OWN00015&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MATUS BUILDING Shop 2
      </td>
      <td class="td_report_small" style="">Mr P Pretorius,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,558.26</td>
      <td class="td_report_small" style="text-align: right">18,441.74</td>
      <td class="td_report_small" style="text-align: right">18,054.73</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">38,054.73</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00014&amp;PID=PRO00221&amp;OID=OWN00015&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MATUS BUILDING Shop 3
      </td>
      <td class="td_report_small" style="">BOIKETLONG FUNERAL DIRECTORS CC</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,938.71</td>
      <td class="td_report_small" style="text-align: right">16,237.33</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">29,176.04</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00042&amp;PID=PRO00222&amp;OID=OWN00089&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">MEDOC Unit 1</td>
      <td class="td_report_small" style="">DR GF JORDAAN</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,163.12</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,163.12</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00523&amp;PID=PRO00554&amp;OID=OWN00089&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">MEDOC UNIT 3</td>
      <td class="td_report_small" style="">DR TJR TOTIWESURGERY (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,637.74</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,637.74</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00438&amp;PID=PRO00516&amp;OID=OWN00089&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">MEDOC UNIT 5</td>
      <td class="td_report_small" style="">KREDO (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,085.39</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,085.39</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00099&amp;PID=PRO00240&amp;OID=OWN00005&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MERRIMAN ARCADE 101
      </td>
      <td class="td_report_small" style="">MARVITE TRADING (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">75,262.25</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">75,262.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00684&amp;PID=PRO00239&amp;OID=OWN00005&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MERRIMAN ARCADE 1
      </td>
      <td class="td_report_small" style="">BIG B CHICKENS CC</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">26,798.52</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">26,798.52</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00309&amp;PID=PRO00242&amp;OID=OWN00005&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MERRIMAN ARCADE 5
      </td>
      <td class="td_report_small" style="">
        RIFT VALLEY IMPORT AND EXPORT (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">19,250.07</td>
      <td class="td_report_small" style="text-align: right">43,099.76</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">62,349.83</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00071&amp;PID=PRO00243&amp;OID=OWN00005&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MERRIMAN ARCADE Shop 11
      </td>
      <td class="td_report_small" style="">Jankie Funeral Services,</td>
      <td class="td_report_small" style="text-align: right">218,793.87</td>
      <td class="td_report_small" style="text-align: right">8,710.95</td>
      <td class="td_report_small" style="text-align: right">8,484.02</td>
      <td class="td_report_small" style="text-align: right">9,450.72</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">245,439.56</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00491&amp;PID=PRO00244&amp;OID=OWN00005&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MERRIMAN ARCADE Shop 2
      </td>
      <td class="td_report_small" style="">EMMA BETHAL GENERAL TRADING</td>
      <td class="td_report_small" style="text-align: right">34,471.08</td>
      <td class="td_report_small" style="text-align: right">7,996.61</td>
      <td class="td_report_small" style="text-align: right">10,557.29</td>
      <td class="td_report_small" style="text-align: right">9,320.69</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">62,345.67</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00588&amp;PID=PRO00536&amp;OID=OWN00117&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MINNAAR STREET 101
      </td>
      <td class="td_report_small" style="">WALTER, M S</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,719.59</td>
      <td class="td_report_small" style="text-align: right">10,287.39</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,006.98</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00683&amp;PID=PRO00632&amp;OID=OWN00175&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">MONICA PLACE 26</td>
      <td class="td_report_small" style="">ADAMS, A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,600.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,600.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00139&amp;PID=PRO00247&amp;OID=OWN00062&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MOTSUMI'S BUILDING Unit 2
      </td>
      <td class="td_report_small" style="">Mr B W Ubisi,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,225.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,225.32</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00598&amp;PID=PRO00529&amp;OID=OWN00062&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MOTSUMI'S BUILDING UNIT 3
      </td>
      <td class="td_report_small" style="">KOOZINA</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,604.27</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,604.27</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00486&amp;PID=PRO00538&amp;OID=OWN00062&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MOTSUMI'S BUILDING UNIT 6
      </td>
      <td class="td_report_small" style="">
        NBH PROPERTIES AND INTELLECTUALS (PTY) LTD T/A RIG
      </td>
      <td class="td_report_small" style="text-align: right">41,882.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">41,882.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00634&amp;PID=PRO00608&amp;OID=OWN00062&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        MOTSUMI'S BUILDING UNIT 7
      </td>
      <td class="td_report_small" style="">
        T RALITLHARE T/A TLHOLO KA MOKOKA CONSULTANTS
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,953.78</td>
      <td class="td_report_small" style="text-align: right">6,405.14</td>
      <td class="td_report_small" style="text-align: right">6,639.24</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,998.16</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00689&amp;PID=PRO00119&amp;OID=OWN00063&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        N&amp;H HOENDERDOS BUI Shop 2
      </td>
      <td class="td_report_small" style="">SYNKHEM SOLUTIONS</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,663.73</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,663.73</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00510&amp;PID=PRO00120&amp;OID=OWN00063&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        N&amp;H HOENDERDOS BUI Shop 3
      </td>
      <td class="td_report_small" style="">STRUB LUBRICANTS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,096.95</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,096.95</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00510&amp;PID=PRO00121&amp;OID=OWN00063&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        N&amp;H HOENDERDOS BUI Unit 1
      </td>
      <td class="td_report_small" style="">STRUB LUBRICANTS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,203.28</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,203.28</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00219&amp;PID=PRO00248&amp;OID=OWN00050&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        NATALIE STREET 10
      </td>
      <td class="td_report_small" style="">WATER WISE FILTRATION (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,261.52</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">17,261.52</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00224&amp;PID=PRO00249&amp;OID=OWN00055&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        NO 10, CLUB 38 10
      </td>
      <td class="td_report_small" style="">Mr S P Havenga,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">99.19</td>
      <td class="td_report_small" style="text-align: right">6,353.50</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,452.69</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00369&amp;PID=PRO00374&amp;OID=OWN00080&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 1 (Utils)
      </td>
      <td class="td_report_small" style="">Wm Brick Force (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">16,956.07</td>
      <td class="td_report_small" style="text-align: right">20,651.05</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">37,607.12</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00028&amp;PID=PRO00251&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 1
      </td>
      <td class="td_report_small" style="">Danmik Power And Construction,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">109,187.76</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">109,187.76</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00619&amp;PID=PRO00252&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 4
      </td>
      <td class="td_report_small" style="">SUPREMECOAT HOLDINGS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,525.12</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,525.12</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00535&amp;PID=PRO00460&amp;OID=OWN00080&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 5 (Utils)
      </td>
      <td class="td_report_small" style="">DANMIK POWER AND CONSTRUCTION</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,056.24</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,056.24</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00534&amp;PID=PRO00250&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 5
      </td>
      <td class="td_report_small" style="">DANMIK POWER AND CONSTRUCTION</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,106.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,106.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00453&amp;PID=PRO00376&amp;OID=OWN00080&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 6 (Utils)
      </td>
      <td class="td_report_small" style="">
        OLIWAVE PROPRIETARY LIMITED (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">216.36</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">216.36</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00068&amp;PID=PRO00377&amp;OID=OWN00080&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 7 (Utils)
      </td>
      <td class="td_report_small" style="">IMMELMAN PLASTICS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">91,930.43</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">91,930.43</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00068&amp;PID=PRO00254&amp;OID=OWN00054&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX1 Unit 7
      </td>
      <td class="td_report_small" style="">IMMELMAN PLASTICS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">70,727.23</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">70,727.23</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00605&amp;PID=PRO00258&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX2 Unit 10 &amp; 11
      </td>
      <td class="td_report_small" style="">CONCIV STRAT (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">52,969.77</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">52,969.77</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00355&amp;PID=PRO00257&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX2 Unit 1
      </td>
      <td class="td_report_small" style="">Vaal Bag Manufactures (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">37,370.55</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">37,370.55</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00497&amp;PID=PRO00259&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX2 Unit 2
      </td>
      <td class="td_report_small" style="">VAAL BULK BAGS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.80</td>
      <td class="td_report_small" style="text-align: right">15,786.58</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,787.38</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00572&amp;PID=PRO00255&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX2 Unit 3
      </td>
      <td class="td_report_small" style="">
        KONECT TELECOMMUNICATIONS (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,811.68</td>
      <td class="td_report_small" style="text-align: right">11,889.57</td>
      <td class="td_report_small" style="text-align: right">12,117.53</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">28,818.78</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00437&amp;PID=PRO00262&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX2 Unit 6
      </td>
      <td class="td_report_small" style="">THULTECH (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,661.98</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,661.98</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00063&amp;PID=PRO00263&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX2 Unit 7
      </td>
      <td class="td_report_small" style="">Hegan / Duxenro Trading,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">100.00</td>
      <td class="td_report_small" style="text-align: right">22,163.09</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">22,263.09</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00046&amp;PID=PRO00256&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        OLIVE BRANCH PARK EX2 Unit 9
      </td>
      <td class="td_report_small" style="">
        Dungbeetles Septic Pumping (pty) Ltd,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,428.43</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,428.43</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00661&amp;PID=PRO00589&amp;OID=OWN00148&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        PLOWMAN STREET 43
      </td>
      <td class="td_report_small" style="">ODOKO CONSTRUCTIONS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00090&amp;PID=PRO00266&amp;OID=OWN00067&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        PROPTEN PROPERTY 2
      </td>
      <td class="td_report_small" style="">LE ROUX STAALWERKE</td>
      <td class="td_report_small" style="text-align: right">18,321.98</td>
      <td class="td_report_small" style="text-align: right">8,114.53</td>
      <td class="td_report_small" style="text-align: right">7,824.82</td>
      <td class="td_report_small" style="text-align: right">8,135.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">42,396.65</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00327&amp;PID=PRO00267&amp;OID=OWN00065&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">RIVERPARK 1</td>
      <td class="td_report_small" style="">Square Deal Auto,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">29,060.55</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">29,060.55</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00415&amp;PID=PRO00497&amp;OID=OWN00113&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">ROOSEVELT 11 A</td>
      <td class="td_report_small" style="">DE VILLIERS, M J</td>
      <td class="td_report_small" style="text-align: right">8,883.68</td>
      <td class="td_report_small" style="text-align: right">177.67</td>
      <td class="td_report_small" style="text-align: right">181.23</td>
      <td class="td_report_small" style="text-align: right">184.85</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,427.43</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00234&amp;PID=PRO00268&amp;OID=OWN00021&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">RUANA COURT 11</td>
      <td class="td_report_small" style="">MR T M BUTHELEZI</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,939.89</td>
      <td class="td_report_small" style="text-align: right">6,655.60</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,595.49</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00227&amp;PID=PRO00273&amp;OID=OWN00027&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">RUANA COURT 8</td>
      <td class="td_report_small" style="">ANTONIO TRIGO, A T</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,515.11</td>
      <td class="td_report_small" style="text-align: right">3,843.50</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,358.61</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00251&amp;PID=PRO00276&amp;OID=OWN00074&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        S. MANN PROPERTIES 1
      </td>
      <td class="td_report_small" style="">MRS M STRYDOM</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,314.10</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,314.10</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00203&amp;PID=PRO00278&amp;OID=OWN00074&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        S. MANN PROPERTIES 3
      </td>
      <td class="td_report_small" style="">Mr P H Van Staden,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,745.64</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">15,745.64</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00517&amp;PID=PRO00279&amp;OID=OWN00011&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SANDSTONE STREET 27
      </td>
      <td class="td_report_small" style="">MPOFU, E</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,693.71</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,693.71</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00665&amp;PID=PRO00619&amp;OID=OWN00165&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SATURN STREET 13, SASOLBURG
      </td>
      <td class="td_report_small" style="">SHARP MED EMS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,476.25</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,476.25</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00066&amp;PID=PRO00284&amp;OID=OWN00075&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SILVER LIGHT BUILDIN 6
      </td>
      <td class="td_report_small" style="">Homefront Trading 94,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,950.15</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">8,950.15</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00296&amp;PID=PRO00289&amp;OID=OWN00075&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SILVER LIGHT BUILDIN Shop 16 &amp; 17
      </td>
      <td class="td_report_small" style="">
        NORTHERN ENCLOSURES &amp; POWDER COATERS (PTY) LTD T/A
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">21,416.78</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">21,416.78</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00466&amp;PID=PRO00290&amp;OID=OWN00075&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SILVER LIGHT BUILDIN Shop 2
      </td>
      <td class="td_report_small" style="">TRAINING PORTAL ONLINE (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">19,707.11</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">19,707.11</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00233&amp;PID=PRO00295&amp;OID=OWN00075&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SILVER LIGHT BUILDIN Shop 9
      </td>
      <td class="td_report_small" style="">MR T I MFEKANE</td>
      <td class="td_report_small" style="text-align: right">10,027.70</td>
      <td class="td_report_small" style="text-align: right">10,917.80</td>
      <td class="td_report_small" style="text-align: right">10,336.16</td>
      <td class="td_report_small" style="text-align: right">10,848.88</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">42,130.54</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00483&amp;PID=PRO00296&amp;OID=OWN00075&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SILVER LIGHT BUILDIN Unit 11
      </td>
      <td class="td_report_small" style="">AUTOBOYS AUTOMOTIVE (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,289.05</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">14,289.05</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00600&amp;PID=PRO00590&amp;OID=OWN00079&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">SPENCE 6</td>
      <td class="td_report_small" style="">
        J AND M COOLING SUPPLIES (PTY) LTD
      </td>
      <td class="td_report_small" style="text-align: right">33,181.98</td>
      <td class="td_report_small" style="text-align: right">32,836.60</td>
      <td class="td_report_small" style="text-align: right">32,510.22</td>
      <td class="td_report_small" style="text-align: right">34,729.94</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">133,258.74</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00306&amp;PID=PRO00298&amp;OID=OWN00078&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SPRINGBOK BUILDING Shop 1
      </td>
      <td class="td_report_small" style="">Redsquare Pub 24/7,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,378.40</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,378.40</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00006&amp;PID=PRO00299&amp;OID=OWN00078&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SPRINGBOK BUILDING Shop 5 &amp; 6
      </td>
      <td class="td_report_small" style="">Anjam And Sons Trading C.c.,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,709.62</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">12,709.62</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00648&amp;PID=PRO00001&amp;OID=OWN00001&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">STEEL 19 Unit 8</td>
      <td class="td_report_small" style="">TRIO BAGS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">42,122.18</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">42,122.18</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00424&amp;PID=PRO00301&amp;OID=OWN00051&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">SUNNYSIDE 2</td>
      <td class="td_report_small" style="">KRUGER, K J</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">447.60</td>
      <td class="td_report_small" style="text-align: right">5,515.75</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,963.35</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00470&amp;PID=PRO00302&amp;OID=OWN00027&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        SUNNYSIDE FLATS 5
      </td>
      <td class="td_report_small" style="">NDLEBE, M P</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">766.68</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">766.68</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00621&amp;PID=PRO00591&amp;OID=OWN00149&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">TAU STREET 436</td>
      <td class="td_report_small" style="">RANTHOKHO, M S</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,648.53</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,648.53</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00131&amp;PID=PRO00304&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK A Unit 1
      </td>
      <td class="td_report_small" style="">Mr A K Mushi,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">40.40</td>
      <td class="td_report_small" style="text-align: right">6,206.05</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,246.45</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00699&amp;PID=PRO00307&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK A Unit 5
      </td>
      <td class="td_report_small" style="">KUMALO, T L</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,981.68</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,981.68</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00712&amp;PID=PRO00308&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK A Unit 6
      </td>
      <td class="td_report_small" style="">PETSANA, T A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,421.05</td>
      <td class="td_report_small" style="text-align: right">5,391.42</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,812.47</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00555&amp;PID=PRO00309&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK A Unit 7
      </td>
      <td class="td_report_small" style="">RAHMAN, R</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,936.40</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,936.40</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00277&amp;PID=PRO00310&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK A Unit 8
      </td>
      <td class="td_report_small" style="">MS N KUBEKA</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">578.06</td>
      <td class="td_report_small" style="text-align: right">5,884.38</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,462.44</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00256&amp;PID=PRO00311&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B Unit 1
      </td>
      <td class="td_report_small" style="">MS A P THAMBO</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.65</td>
      <td class="td_report_small" style="text-align: right">5,540.41</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,541.06</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00623&amp;PID=PRO00598&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B UNIT 2
      </td>
      <td class="td_report_small" style="">MOSA, C</td>
      <td class="td_report_small" style="text-align: right">16,425.67</td>
      <td class="td_report_small" style="text-align: right">5,608.51</td>
      <td class="td_report_small" style="text-align: right">5,570.68</td>
      <td class="td_report_small" style="text-align: right">5,835.10</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">33,439.96</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00704&amp;PID=PRO00454&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B UNIT 3
      </td>
      <td class="td_report_small" style="">TSHABANGU, N</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">102.60</td>
      <td class="td_report_small" style="text-align: right">5,132.05</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,234.65</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00159&amp;PID=PRO00335&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B Unit 4
      </td>
      <td class="td_report_small" style="">Mr I P Soetmelk,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,292.37</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,292.37</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00394&amp;PID=PRO00313&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B Unit 5
      </td>
      <td class="td_report_small" style="">MOLOI, M E</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,239.00</td>
      <td class="td_report_small" style="text-align: right">5,718.18</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,957.18</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00271&amp;PID=PRO00314&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B Unit 6
      </td>
      <td class="td_report_small" style="">Ms M Tom,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">203.65</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">203.65</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00577&amp;PID=PRO00315&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B Unit 7
      </td>
      <td class="td_report_small" style="">NGOSHI, J K</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,130.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,130.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00433&amp;PID=PRO00316&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK B Unit 8
      </td>
      <td class="td_report_small" style="">CINDI, P M</td>
      <td class="td_report_small" style="text-align: right">30,696.08</td>
      <td class="td_report_small" style="text-align: right">4,763.92</td>
      <td class="td_report_small" style="text-align: right">4,709.20</td>
      <td class="td_report_small" style="text-align: right">4,956.38</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">45,125.58</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00508&amp;PID=PRO00317&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 1
      </td>
      <td class="td_report_small" style="">ZENDAGYSTIX (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,540.40</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,540.40</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00636&amp;PID=PRO00333&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 2
      </td>
      <td class="td_report_small" style="">RANGAZA, Z M</td>
      <td class="td_report_small" style="text-align: right">319.82</td>
      <td class="td_report_small" style="text-align: right">5,386.40</td>
      <td class="td_report_small" style="text-align: right">5,344.12</td>
      <td class="td_report_small" style="text-align: right">5,504.01</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">16,554.35</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00283&amp;PID=PRO00318&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 3
      </td>
      <td class="td_report_small" style="">Ms P P Letlaka,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,205.24</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,205.24</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00566&amp;PID=PRO00319&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 4
      </td>
      <td class="td_report_small" style="">ABDULAHI, A</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,826.98</td>
      <td class="td_report_small" style="text-align: right">6,929.54</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,756.52</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00440&amp;PID=PRO00320&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 5
      </td>
      <td class="td_report_small" style="">YEYE'S ENTERPRISES</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,653.90</td>
      <td class="td_report_small" style="text-align: right">5,806.18</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,460.08</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00177&amp;PID=PRO00321&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 6
      </td>
      <td class="td_report_small" style="">Mr K P Malele,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1.65</td>
      <td class="td_report_small" style="text-align: right">5,540.43</td>
      <td class="td_report_small" style="text-align: right">5,804.24</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,346.32</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00269&amp;PID=PRO00322&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 7
      </td>
      <td class="td_report_small" style="">Ms M Ramaotswa,</td>
      <td class="td_report_small" style="text-align: right">3,992.46</td>
      <td class="td_report_small" style="text-align: right">5,870.25</td>
      <td class="td_report_small" style="text-align: right">5,737.65</td>
      <td class="td_report_small" style="text-align: right">6,005.41</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">21,605.77</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00664&amp;PID=PRO00323&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK C Unit 8
      </td>
      <td class="td_report_small" style="">JACOBS, A C</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">20.00</td>
      <td class="td_report_small" style="text-align: right">5,283.40</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,303.40</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00388&amp;PID=PRO00465&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK D UNIT 2
      </td>
      <td class="td_report_small" style="">KOOPMAN, M F</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,040.00</td>
      <td class="td_report_small" style="text-align: right">4,213.80</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,253.80</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00255&amp;PID=PRO00325&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK D Unit 3
      </td>
      <td class="td_report_small" style="">Ms A Ntshobane,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,833.84</td>
      <td class="td_report_small" style="text-align: right">5,874.07</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,707.91</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00128&amp;PID=PRO00326&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK D Unit 6
      </td>
      <td class="td_report_small" style="">Mr A D Mola,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,384.42</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,384.42</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00285&amp;PID=PRO00327&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK D Unit 7
      </td>
      <td class="td_report_small" style="">Ms R K Dithejane,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,402.71</td>
      <td class="td_report_small" style="text-align: right">5,801.45</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,204.16</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00624&amp;PID=PRO00446&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK D UNIT 8
      </td>
      <td class="td_report_small" style="">FOSTER, J</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,770.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,770.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00265&amp;PID=PRO00328&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK E Unit 2
      </td>
      <td class="td_report_small" style="">Ms M C Mathalemele,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,833.43</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2,833.43</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00264&amp;PID=PRO00329&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK E Unit 3
      </td>
      <td class="td_report_small" style="">Ms L T Setai,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,540.40</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,540.40</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00657&amp;PID=PRO00330&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK E Unit 4
      </td>
      <td class="td_report_small" style="">TAGANE, L E</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">252.60</td>
      <td class="td_report_small" style="text-align: right">5,135.05</td>
      <td class="td_report_small" style="text-align: right">5,390.75</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">10,778.40</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00703&amp;PID=PRO00337&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK E Unit 5
      </td>
      <td class="td_report_small" style="">MSIBI, R C</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">143.34</td>
      <td class="td_report_small" style="text-align: right">5,132.87</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,276.21</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00058&amp;PID=PRO00338&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK E Unit 6
      </td>
      <td class="td_report_small" style="">JOOSTE, M V</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,400.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,400.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00176&amp;PID=PRO00339&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK E Unit 7
      </td>
      <td class="td_report_small" style="">MR K J KOTJANE</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,000.00</td>
      <td class="td_report_small" style="text-align: right">6,156.63</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,156.63</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00434&amp;PID=PRO00331&amp;OID=OWN00069&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE BARN BLOCK E Unit 8
      </td>
      <td class="td_report_small" style="">SABELA, H P</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,011.80</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,011.80</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00680&amp;PID=PRO00630&amp;OID=OWN00173&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        THE WILLOWS NO 11, THREE RIVERS
      </td>
      <td class="td_report_small" style="">MABUNDA, G V</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,370.43</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,370.43</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00730&amp;PID=PRO00382&amp;OID=OWN00013&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">VILLA NONGANA 1</td>
      <td class="td_report_small" style="">SMITH, B C</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,500.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">7,500.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00031&amp;PID=PRO00383&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 - ARREAR A Shop 44 A
      </td>
      <td class="td_report_small" style="">DECKEL SPORTSLIDS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">741,882.35</td>
      <td class="td_report_small" style="text-align: right">15,137.65</td>
      <td class="td_report_small" style="text-align: right">15,140.40</td>
      <td class="td_report_small" style="text-align: right">15,443.21</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">787,603.61</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00300&amp;PID=PRO00384&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL 11
      </td>
      <td class="td_report_small" style="">Phalazisa Cc,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">32,341.64</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">32,341.64</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00090&amp;PID=PRO00385&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL 18
      </td>
      <td class="td_report_small" style="">LE ROUX STAALWERKE</td>
      <td class="td_report_small" style="text-align: right">220.49</td>
      <td class="td_report_small" style="text-align: right">20.85</td>
      <td class="td_report_small" style="text-align: right">21.27</td>
      <td class="td_report_small" style="text-align: right">21.69</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">284.30</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00326&amp;PID=PRO00386&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL 23
      </td>
      <td class="td_report_small" style="">
        Spiral Hydraulic &amp; Engineering Services,
      </td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,194.33</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,194.33</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00054&amp;PID=PRO00388&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL 42
      </td>
      <td class="td_report_small" style="">Fedmech Cc,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">1,398.19</td>
      <td class="td_report_small" style="text-align: right">1,732.15</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,130.34</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00067&amp;PID=PRO00390&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL 7
      </td>
      <td class="td_report_small" style="">Hydro Rubber (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,712.70</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">6,712.70</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00300&amp;PID=PRO00392&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 12
      </td>
      <td class="td_report_small" style="">Phalazisa Cc,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">2.00</td>
      <td class="td_report_small" style="text-align: right">11,768.75</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">11,770.75</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00368&amp;PID=PRO00393&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 14
      </td>
      <td class="td_report_small" style="">Wikid Products (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,593.74</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">5,593.74</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00025&amp;PID=PRO00395&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 21
      </td>
      <td class="td_report_small" style="">CRUDUS WASTE MANAGEMENT</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">23,439.88</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">23,439.88</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00310&amp;PID=PRO00397&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 25A
      </td>
      <td class="td_report_small" style="">RONA'S TUCK SHOP</td>
      <td class="td_report_small" style="text-align: right">484.63</td>
      <td class="td_report_small" style="text-align: right">2,879.28</td>
      <td class="td_report_small" style="text-align: right">2,866.12</td>
      <td class="td_report_small" style="text-align: right">2,811.44</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,041.47</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00382&amp;PID=PRO00459&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL SHOP 25
      </td>
      <td class="td_report_small" style="">ATC (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">13,107.81</td>
      <td class="td_report_small" style="text-align: right">23,746.51</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">36,854.32</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00518&amp;PID=PRO00467&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL SHOP 26
      </td>
      <td class="td_report_small" style="">MOKOENA, L</td>
      <td class="td_report_small" style="text-align: right">30,366.25</td>
      <td class="td_report_small" style="text-align: right">34,269.03</td>
      <td class="td_report_small" style="text-align: right">32,446.41</td>
      <td class="td_report_small" style="text-align: right">32,501.33</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">129,583.02</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00446&amp;PID=PRO00519&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 42 A
      </td>
      <td class="td_report_small" style="">DECKEL SPORTSLIDS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">9,315.00</td>
      <td class="td_report_small" style="text-align: right">9,315.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,630.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00031&amp;PID=PRO00399&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 44
      </td>
      <td class="td_report_small" style="">DECKEL SPORTSLIDS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">192,979.95</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">192,979.95</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00387&amp;PID=PRO00464&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL SHOP 4
      </td>
      <td class="td_report_small" style="">VENTER, BJ</td>
      <td class="td_report_small" style="text-align: right">18,733.78</td>
      <td class="td_report_small" style="text-align: right">7,637.44</td>
      <td class="td_report_small" style="text-align: right">5,869.20</td>
      <td class="td_report_small" style="text-align: right">6,242.59</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">38,483.01</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00031&amp;PID=PRO00402&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 54
      </td>
      <td class="td_report_small" style="">DECKEL SPORTSLIDS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">16,619.32</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">16,619.32</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00067&amp;PID=PRO00401&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Shop 5
      </td>
      <td class="td_report_small" style="">Hydro Rubber (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,587.98</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">3,587.98</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00725&amp;PID=PRO00403&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Unit 32
      </td>
      <td class="td_report_small" style="">DECKEL SPORTSLIDS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,174.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,174.00</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00031&amp;PID=PRO00404&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Unit 43
      </td>
      <td class="td_report_small" style="">DECKEL SPORTSLIDS (PTY) LTD</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">65,373.50</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">65,373.50</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00096&amp;PID=PRO00405&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL Unit 45
      </td>
      <td class="td_report_small" style="">Lwp Trading (pty) Ltd,</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">441,403.56</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">441,403.56</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00532&amp;PID=PRO00559&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL UNITS 19A 47 67 6
      </td>
      <td class="td_report_small" style="">MUMPANPAN LOGISTICS CC</td>
      <td class="td_report_small" style="text-align: right">172,801.63</td>
      <td class="td_report_small" style="text-align: right">59,888.54</td>
      <td class="td_report_small" style="text-align: right">59,097.81</td>
      <td class="td_report_small" style="text-align: right">58,994.18</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">350,782.16</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00538&amp;PID=PRO00562&amp;OID=OWN00083&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        VISION 21 INDUSTRIAL
      </td>
      <td class="td_report_small" style="">KISS LOGISTICS - ARREARS</td>
      <td class="td_report_small" style="text-align: right">129,166.63</td>
      <td class="td_report_small" style="text-align: right">20,833.33</td>
      <td class="td_report_small" style="text-align: right">20,833.33</td>
      <td class="td_report_small" style="text-align: right">20,833.33</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">191,666.62</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00286&amp;PID=PRO00406&amp;OID=OWN00053&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">WESTON PARK 13</td>
      <td class="td_report_small" style="">MS R MAKHOBA</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,086.94</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">4,086.94</td>
    </tr>
    <tr
      name="trLineClick"
      slineclick="https://rms.propertysuite.co.za/Reports/Tenants/TenantMonthly.aspx?TID=TEN00667&amp;PID=PRO00618&amp;OID=OWN00166&amp;STD=01052023&amp;EDD=31082023"
      sgreyplaceholder=""
    >
      <td class="td_report_small" style="border-right: 0px">
        WITTERBERG NO 7 SE 8, VANDERBIJLPARK CENTRAL
      </td>
      <td class="td_report_small" style="">MABITSELA, M T</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,172.17</td>
      <td class="td_report_small" style="text-align: right">0.00</td>
      <td class="td_report_small" style="text-align: right">18,172.17</td>
    </tr>
    <tr sgreyplaceholder="">
      <th colspan="2" class="td_report_small" style="text-align: left">
        Totals :
      </th>
      <th class="td_report_small" style="text-align: right">4,317,113.26</th>
      <th class="td_report_small" style="text-align: right">779,470.09</th>
      <th class="td_report_small" style="text-align: right">1,098,519.88</th>
      <th class="td_report_small" style="text-align: right">4,495,674.99</th>
      <th class="td_report_small" style="text-align: right">0.00</th>
      <th class="td_report_small" style="text-align: right">10,690,778.22</th>
    </tr>
    <tr>
      <th colspan="8" class="td_report"></th>
    </tr>
  </tbody>
</table>

'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <tr> elements with the 'slineclick' attribute
slineclick_elements = soup.find_all('tr', attrs={'slineclick': True})

# Extract the 'slineclick' properties and join them with newlines
slineclick_properties = "\n".join(element['slineclick'] for element in slineclick_elements)

# Copy the extracted properties to the clipboard
pyperclip.copy(slineclick_properties)

print("slineclick properties have been copied to the clipboard.")
