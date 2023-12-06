import re
from io import BytesIO
from xhtml2pdf import pisa
from django.core.files.base import ContentFile

html = """
<!DOCTYPE html>
<html>
 <head id="ctl00_Head1">
  <title>
   Tenant Statement
  </title>
  <link href="https://rms.propertysuite.co.za/stylesheets/Reports_02.css?v=005" rel="stylesheet" type="text/css"/>
  <meta charset="utf-8"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="-1" http-equiv="Expires"/>
  <meta content="no-cache" http-equiv="Pragma"/>
  <meta content="no-cache, no-store, must-revalidate" http-equiv="Cache-Control"/>
  <meta content="SKYPE_TOOLBAR_PARSER_COMPATIBLE" name="SKYPE_TOOLBAR"/>
  <!--<meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE" />-->
 </head>
 <body>
  <table style="width:100%;">
   <tr>
    <td>
     <form action="./TenantMonthly.aspx?TID=TEN00005&amp;PID=PRO00258&amp;OID=OWN00079&amp;STD=01032022&amp;EDD=28022023" id="aspnetForm" method="post" name="aspnetForm">
      <input id="__VIEWSTATE" name="__VIEWSTATE" type="hidden" value="/wEPDwULLTIwODEyODU3ODYPZBYCZg9kFgICAw9kFgJmD2QWCGYPZBYCAgEPDxYCHgdWaXNpYmxlZ2RkAgEPDxYCHwBnZBYCAgEPDxYCHwBnZGQCAg9kFgICAQ8PFgIfAGdkZAIFDw8WAh8AZ2RkZEC+AJR2UbqY8iw6Mf1m+LdNrScLvPCMhxBtrfFbJtkN"/>
      <input id="__VIEWSTATEGENERATOR" name="__VIEWSTATEGENERATOR" type="hidden" value="4C0562D0"/>
      <input id="__EVENTVALIDATION" name="__EVENTVALIDATION" type="hidden" value="/wEdACz42lQztTR//4JBjQrZzwoMPgA43k/VWmuffsI7lyxrxeBBptMMrOcrYPBwX26wbyipTlXOK7P9AXMhCQVIjHefwIG0B75f+EPCxmT16zUxF7v81Q3IxHVNisxjwSL2YYbH1aVv5e1FKzEPZcTz/uLf00885M4tIHHOUzTQlzbl0SKNP2USAwNgklGUiZek0Z7i6JQT4hWuoBjjVgMA1TjcO6cgqWFhrhn1MS3eBFflerGcIEUrG3ou88uXWu7GwEQs5mgcvKr2G8aM/ZwgWl4Nn46V9OPQrRgEt72940wkiP+Ep2OtzrZb2ch0tyhjRmD4tMNLgf76u/l4JB0Ku5i6PnWfSMADeRI1SnqYIE8NVr/LLcsRFBDmLc77W7ubs1Idc2YMfJowd+U7RSnW5GchWkf3U4Fov9mN88MXS2nvkDBpy+/jHI1s9vzAYKTRFPizfixsEi7spLQRWItswYQjtg1TQIwz0wOXBamuj2uOfX67zlWZ6X36v45wkzdGnGfKao3jAREYynN2dzlnZJ/JTnANXQu+Ik9cYaC6a6w0PSgXeya4o/rIL4QT0F198cpHDUYQ93R8nKJXcQmgUS7nDlyRtESQ0gmhIwLjXIn3Iq5NS9LCZrwIR+D7m7Hf0OfcsldnITz/pF3Fg5kMT6BzxKgMLWrh9nJDTN4F/JKhupjWgQ+2RpWAhTurlpCb6bXkSJt+7YrsQ5FNkjqvLxzIKMCK8GTVoe5H0Ku1+W6V2v3wf3m0FT8EVTseq71YSTt10NAVOw0jvzfZ4mOpeEFJx4AFyVxECzhQ5tSpLafkjKKB6jBN0HVH4GfYDLJD67QDIxrKzvrdSyCuPLr8tYya9FlaVkj6KR1Ywh1qq/CCLBM8dkm5rVYoB4iSz8GTgUd8IcglLx6awFfBjR52vnr0AeuCyN/ytmcjFvPji0aTPr+YP1i70LxFZ5lsA79wcnGW4/4I7ob1s2DfKHoOVVan"/>
      <div>
       <img alt="letterhead" src="https://rms.propertysuite.co.za/Images/Display.aspx?SOURCE=Company&amp;HF=H&amp;CID=557"/>
       <p>
        Company Reg Number : 2020/125835/07
       </p>
       <p>
        VAT Number : 4640295574
       </p>
       <div style="width: 100%;">
        <div id="ctl00_ContentPlaceHolder1_pTENStatementVersion02">
         <div style=" font-size:larger; font-weight:bold ; text-decoration:underline; width: 100%; ">
          <center>
           TENANT STATEMENT / TAX INVOICE
          </center>
         </div>
         <table width="100%">
          <tr>
           <td>
            <div>
             <table border="1" class="table_report">
              <tr>
               <th class="td_report">
                STATEMENT TO:
               </th>
               <th class="td_report">
                FOR PROPERTY:
               </th>
              </tr>
              <tr>
               <td class="td_report">
                Anchor Pallets (pty) Ltd,
                <br/>
               </td>
               <td class="td_report">
                OLIVE BRANCH PARK EX2 Unit 10 &amp; 11
               </td>
              </tr>
             </table>
            </div>
           </td>
           <td>
            <div style=" text-align:right; float:right ">
             <table border="1" class="table_report">
              <tr>
               <th class="td_report" style="text-align:center ">
                DATE RANGE
               </th>
               <th class="td_report" style="text-align:center ">
                OUR REF
               </th>
              </tr>
              <tr>
               <td class="td_report" edd="28/02/2023" edit="YES" ifd="YES" name="stddate" pdf="YES" pdftype="TenantMonthly" show="YES" std="01/03/2022" stversion="TENMONTHLY">
                01/03/2022 - 28/02/2023
               </td>
               <td class="td_report">
                TEN00005 - 00079
               </td>
              </tr>
             </table>
            </div>
           </td>
          </tr>
         </table>
         <div style=" font-size: xx-small ">
          <center>
          </center>
         </div>
         <div id="ctl00_ContentPlaceHolder1_pTENDepositVersion04_02">
          <br>
           <div style="font-size:larger;">
            DEPOSIT STATUS:
           </div>
           <div style="font-size:smaller;">
            MINIMUM DEPOSIT PAYABLE AS PER CONTRACT 6,603.30
           </div>
           <div>
            <table border="1" class="table_report" width="100%">
             <!--<tr><th class=td_report>Description</th><th width="80px" class=td_report>Amount</th></tr>    -->
             <tr>
              <th class="td_report">
               Description
              </th>
              <th class="td_report" style="text-align:right" width="80px">
               Dr (Out)
              </th>
              <th class="td_report" style="text-align:right" width="80px">
               Cr (In)
              </th>
             </tr>
             <tr name="trLineClick" slineclick="TenantDeposit.aspx?TID=TEN00005&amp;PID=PRO00258&amp;OID=OWN00079&amp;STD=01032022&amp;EDD=28022023">
              <td class="td_report">
               DEPOSIT CHARGED
              </td>
              <td class="td_report" style="text-align:right;" width="80px">
               0.00
              </td>
              <td class="td_report" style="text-align:right;" width="80px">
              </td>
             </tr>
            </table>
           </div>
           <br/>
          </br>
         </div>
         <div style=" font-size:medium; font-weight:bold ; text-decoration:underline ">
          TRANSACTIONS:
         </div>
         <!--<div style=" font-size: xx-small "><center>&nbsp;</center></div>-->
         <div>
          <table border="1" class="table_report" width="100%">
           <tr>
            <th class="td_report">
             Transaction #
            </th>
            <th class="td_report">
             Description
            </th>
            <th class="td_report">
             Date
            </th>
            <th class="td_report" width="70px">
             VAT
            </th>
            <th class="td_report" width="70px">
             Dr (Out)
            </th>
            <th class="td_report" width="70px">
             Cr (In)
            </th>
            <th class="td_report" width="70px">
             Balance
            </th>
           </tr>
           <tr>
            <td class="td_report_small" name="obalance">
            </td>
            <td class="td_report">
             OPENING BALANCE
            </td>
            <td class="td_report">
             01/03/2022
            </td>
            <td class="td_report" style="text-align:right" width="70px">
            </td>
            <td class="td_report" style="text-align:right" width="70px">
             3,041.44
            </td>
            <td class="td_report" style="text-align:right" width="70px">
            </td>
            <td class="td_report" style="text-align:right" width="70px">
             3,041.44
            </td>
           </tr>
           <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0016692">
            <td class="td_report_small" name="transno" tno="PRO00258RRENT0000008" trnid="42502521">
             PRO00258
             <br/>
             RRENT0000008
            </td>
            <td class="td_report">
             INV0016692 - RENT CHARGED
            </td>
            <td class="td_report">
             01/03/2022
            </td>
            <td class="td_report" style="text-align:right" width="70px">
             3,847.80
            </td>
            <td class="td_report" style="text-align:right" width="70px">
             29,499.80
            </td>
            <td class="td_report" style="text-align:right" width="70px">
            </td>
            <td class="td_report" style="text-align:right" width="70px">
             32,541.24
            </td>
            <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0016963">
             <td class="td_report_small" name="transno" tno="PRO00258TENMRD0000007" trnid="42503319">
              PRO00258
              <br/>
              TENMRD0000007
             </td>
             <td class="td_report">
              INV0016963 - METER READING FEE
             </td>
             <td class="td_report">
              01/03/2022
             </td>
             <td class="td_report" style="text-align:right" width="70px">
              18.75
             </td>
             <td class="td_report" style="text-align:right" width="70px">
              143.75
             </td>
             <td class="td_report" style="text-align:right" width="70px">
             </td>
             <td class="td_report" style="text-align:right" width="70px">
              32,684.99
             </td>
             <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0017608">
              <td class="td_report_small" name="transno" tno="PRO00258RMS0000030" trnid="42536361">
               PRO00258
               <br/>
               RMS0000030
              </td>
              <td class="td_report">
               INV0017608 - ELECTRICITY MAXIMUM DEMAND 80 UNITS
              </td>
              <td class="td_report">
               01/03/2022
              </td>
              <td class="td_report" style="text-align:right" width="70px">
               4,844.66
              </td>
              <td class="td_report" style="text-align:right" width="70px">
               37,142.40
              </td>
              <td class="td_report" style="text-align:right" width="70px">
              </td>
              <td class="td_report" style="text-align:right" width="70px">
               69,827.39
              </td>
              <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0017609">
               <td class="td_report_small" name="transno" tno="PRO00258RMS0000031" trnid="42536363">
                PRO00258
                <br/>
                RMS0000031
               </td>
               <td class="td_report">
                INV0017609 - WATER
               </td>
               <td class="td_report">
                01/03/2022
               </td>
               <td class="td_report" style="text-align:right" width="70px">
                318.26
               </td>
               <td class="td_report" style="text-align:right" width="70px">
                2,440.00
               </td>
               <td class="td_report" style="text-align:right" width="70px">
               </td>
               <td class="td_report" style="text-align:right" width="70px">
                72,267.39
               </td>
               <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0017610">
                <td class="td_report_small" name="transno" tno="PRO00258RMS0000032" trnid="42536365">
                 PRO00258
                 <br/>
                 RMS0000032
                </td>
                <td class="td_report">
                 INV0017610 - ELECTRICITY 571029-577644
                </td>
                <td class="td_report">
                 01/03/2022
                </td>
                <td class="td_report" style="text-align:right" width="70px">
                 2,565.05
                </td>
                <td class="td_report" style="text-align:right" width="70px">
                 19,665.35
                </td>
                <td class="td_report" style="text-align:right" width="70px">
                </td>
                <td class="td_report" style="text-align:right" width="70px">
                 91,932.74
                </td>
                <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0018228">
                 <td class="td_report_small" name="transno" tno="PRO00258RMS0000033" trnid="42861778">
                  PRO00258
                  <br/>
                  RMS0000033
                 </td>
                 <td class="td_report">
                  INV0018228 - ADDITIONAL YARD SPACE
                 </td>
                 <td class="td_report">
                  01/03/2022
                 </td>
                 <td class="td_report" style="text-align:right" width="70px">
                  238.50
                 </td>
                 <td class="td_report" style="text-align:right" width="70px">
                  1,828.50
                 </td>
                 <td class="td_report" style="text-align:right" width="70px">
                 </td>
                 <td class="td_report" style="text-align:right" width="70px">
                  93,761.24
                 </td>
                 <tr>
                  <td class="td_report_small" name="transno" tno="PRO00258RENT0000012" trnid="43036486">
                   PRO00258
                   <br/>
                   RENT0000012
                  </td>
                  <td class="td_report">
                   PAYMENT RECEIVED
                  </td>
                  <td class="td_report">
                   07/03/2022
                  </td>
                  <td class="td_report" style="text-align:right" width="70px">
                   0.00
                  </td>
                  <td class="td_report" style="text-align:right" width="70px">
                  </td>
                  <td class="td_report" style="text-align:right" width="70px">
                   93,761.24
                  </td>
                  <td class="td_report" style="text-align:right" width="70px">
                   0.00
                  </td>
                  <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0019037">
                   <td class="td_report_small" name="transno" tno="PRO00258RRENT0000009" trnid="43130413">
                    PRO00258
                    <br/>
                    RRENT0000009
                   </td>
                   <td class="td_report">
                    INV0019037 - RENT CHARGED
                   </td>
                   <td class="td_report">
                    01/04/2022
                   </td>
                   <td class="td_report" style="text-align:right" width="70px">
                    3,847.80
                   </td>
                   <td class="td_report" style="text-align:right" width="70px">
                    29,499.80
                   </td>
                   <td class="td_report" style="text-align:right" width="70px">
                   </td>
                   <td class="td_report" style="text-align:right" width="70px">
                    29,499.80
                   </td>
                   <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0019599">
                    <td class="td_report_small" name="transno" tno="PRO00258TENMRD0000008" trnid="43131887">
                     PRO00258
                     <br/>
                     TENMRD0000008
                    </td>
                    <td class="td_report">
                     INV0019599 - METER READING FEE
                    </td>
                    <td class="td_report">
                     01/04/2022
                    </td>
                    <td class="td_report" style="text-align:right" width="70px">
                     18.75
                    </td>
                    <td class="td_report" style="text-align:right" width="70px">
                     143.75
                    </td>
                    <td class="td_report" style="text-align:right" width="70px">
                    </td>
                    <td class="td_report" style="text-align:right" width="70px">
                     29,643.55
                    </td>
                    <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0019839">
                     <td class="td_report_small" name="transno" tno="PRO00258RMS0000035" trnid="43161657">
                      PRO00258
                      <br/>
                      RMS0000035
                     </td>
                     <td class="td_report">
                      INV0019839 - ELECTRICITY MAXIMUM DEMAND 80 UNITS
                     </td>
                     <td class="td_report">
                      01/04/2022
                     </td>
                     <td class="td_report" style="text-align:right" width="70px">
                      4,844.66
                     </td>
                     <td class="td_report" style="text-align:right" width="70px">
                      37,142.40
                     </td>
                     <td class="td_report" style="text-align:right" width="70px">
                     </td>
                     <td class="td_report" style="text-align:right" width="70px">
                      66,785.95
                     </td>
                     <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0019840">
                      <td class="td_report_small" name="transno" tno="PRO00258RMS0000036" trnid="43161659">
                       PRO00258
                       <br/>
                       RMS0000036
                      </td>
                      <td class="td_report">
                       INV0019840 - WATER
                      </td>
                      <td class="td_report">
                       01/04/2022
                      </td>
                      <td class="td_report" style="text-align:right" width="70px">
                       318.26
                      </td>
                      <td class="td_report" style="text-align:right" width="70px">
                       2,440.00
                      </td>
                      <td class="td_report" style="text-align:right" width="70px">
                      </td>
                      <td class="td_report" style="text-align:right" width="70px">
                       69,225.95
                      </td>
                      <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0019841">
                       <td class="td_report_small" name="transno" tno="PRO00258RMS0000037" trnid="43161661">
                        PRO00258
                        <br/>
                        RMS0000037
                       </td>
                       <td class="td_report">
                        INV0019841 - ELECTRICITY 588644-602832
                       </td>
                       <td class="td_report">
                        01/04/2022
                       </td>
                       <td class="td_report" style="text-align:right" width="70px">
                        2,624.94
                       </td>
                       <td class="td_report" style="text-align:right" width="70px">
                        20,124.54
                       </td>
                       <td class="td_report" style="text-align:right" width="70px">
                       </td>
                       <td class="td_report" style="text-align:right" width="70px">
                        89,350.49
                       </td>
                       <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0020448">
                        <td class="td_report_small" name="transno" tno="PRO00258RMS0000038" trnid="43409971">
                         PRO00258
                         <br/>
                         RMS0000038
                        </td>
                        <td class="td_report">
                         INV0020448 - ADDITIONAL YARD SPACE
                        </td>
                        <td class="td_report">
                         01/04/2022
                        </td>
                        <td class="td_report" style="text-align:right" width="70px">
                         238.50
                        </td>
                        <td class="td_report" style="text-align:right" width="70px">
                         1,828.50
                        </td>
                        <td class="td_report" style="text-align:right" width="70px">
                        </td>
                        <td class="td_report" style="text-align:right" width="70px">
                         91,178.99
                        </td>
                        <tr>
                         <td class="td_report_small" name="transno" tno="PRO00258RENT0000013" trnid="43844631">
                          PRO00258
                          <br/>
                          RENT0000013
                         </td>
                         <td class="td_report">
                          PAYMENT RECEIVED
                         </td>
                         <td class="td_report">
                          07/04/2022
                         </td>
                         <td class="td_report" style="text-align:right" width="70px">
                          0.00
                         </td>
                         <td class="td_report" style="text-align:right" width="70px">
                         </td>
                         <td class="td_report" style="text-align:right" width="70px">
                          91,178.99
                         </td>
                         <td class="td_report" style="text-align:right" width="70px">
                          0.00
                         </td>
                         <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0021420">
                          <td class="td_report_small" name="transno" tno="PRO00258RRENT0000010" trnid="43929872">
                           PRO00258
                           <br/>
                           RRENT0000010
                          </td>
                          <td class="td_report">
                           INV0021420 - RENT CHARGED
                          </td>
                          <td class="td_report">
                           01/05/2022
                          </td>
                          <td class="td_report" style="text-align:right" width="70px">
                           3,847.80
                          </td>
                          <td class="td_report" style="text-align:right" width="70px">
                           29,499.80
                          </td>
                          <td class="td_report" style="text-align:right" width="70px">
                          </td>
                          <td class="td_report" style="text-align:right" width="70px">
                           29,499.80
                          </td>
                          <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0021788">
                           <td class="td_report_small" name="transno" tno="PRO00258RMS0000039" trnid="43931454">
                            PRO00258
                            <br/>
                            RMS0000039
                           </td>
                           <td class="td_report">
                            INV0021788 - ADDITIONAL YARD SPACE
                           </td>
                           <td class="td_report">
                            01/05/2022
                           </td>
                           <td class="td_report" style="text-align:right" width="70px">
                            238.50
                           </td>
                           <td class="td_report" style="text-align:right" width="70px">
                            1,828.50
                           </td>
                           <td class="td_report" style="text-align:right" width="70px">
                           </td>
                           <td class="td_report" style="text-align:right" width="70px">
                            31,328.30
                           </td>
                           <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0021991">
                            <td class="td_report_small" name="transno" tno="PRO00258TENMRD0000009" trnid="43932354">
                             PRO00258
                             <br/>
                             TENMRD0000009
                            </td>
                            <td class="td_report">
                             INV0021991 - METER READING FEE
                            </td>
                            <td class="td_report">
                             01/05/2022
                            </td>
                            <td class="td_report" style="text-align:right" width="70px">
                             18.75
                            </td>
                            <td class="td_report" style="text-align:right" width="70px">
                             143.75
                            </td>
                            <td class="td_report" style="text-align:right" width="70px">
                            </td>
                            <td class="td_report" style="text-align:right" width="70px">
                             31,472.05
                            </td>
                            <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0022338">
                             <td class="td_report_small" name="transno" tno="PRO00258RMS0000040" trnid="43987962">
                              PRO00258
                              <br/>
                              RMS0000040
                             </td>
                             <td class="td_report">
                              INV0022338 - WATER
                             </td>
                             <td class="td_report">
                              01/05/2022
                             </td>
                             <td class="td_report" style="text-align:right" width="70px">
                              318.26
                             </td>
                             <td class="td_report" style="text-align:right" width="70px">
                              2,440.00
                             </td>
                             <td class="td_report" style="text-align:right" width="70px">
                             </td>
                             <td class="td_report" style="text-align:right" width="70px">
                              33,912.05
                             </td>
                             <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0022340">
                              <td class="td_report_small" name="transno" tno="PRO00258RMS0000041" trnid="43987970">
                               PRO00258
                               <br/>
                               RMS0000041
                              </td>
                              <td class="td_report">
                               INV0022340 - ELECTRICITY MAXIMUM DEMAND 85 UNITS
                              </td>
                              <td class="td_report">
                               01/05/2022
                              </td>
                              <td class="td_report" style="text-align:right" width="70px">
                               5,147.45
                              </td>
                              <td class="td_report" style="text-align:right" width="70px">
                               39,463.80
                              </td>
                              <td class="td_report" style="text-align:right" width="70px">
                              </td>
                              <td class="td_report" style="text-align:right" width="70px">
                               73,375.85
                              </td>
                              <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0022342">
                               <td class="td_report_small" name="transno" tno="PRO00258RMS0000042" trnid="43988050">
                                PRO00258
                                <br/>
                                RMS0000042
                               </td>
                               <td class="td_report">
                                INV0022342 - ELECTRICITY 602832-618792
                               </td>
                               <td class="td_report">
                                01/05/2022
                               </td>
                               <td class="td_report" style="text-align:right" width="70px">
                                3,976.12
                               </td>
                               <td class="td_report" style="text-align:right" width="70px">
                                30,483.60
                               </td>
                               <td class="td_report" style="text-align:right" width="70px">
                               </td>
                               <td class="td_report" style="text-align:right" width="70px">
                                103,859.45
                               </td>
                               <tr>
                                <td class="td_report_small" name="transno" tno="PRO00258RENT0000014" trnid="44458612">
                                 PRO00258
                                 <br/>
                                 RENT0000014
                                </td>
                                <td class="td_report">
                                 PAYMENT RECEIVED
                                </td>
                                <td class="td_report">
                                 05/05/2022
                                </td>
                                <td class="td_report" style="text-align:right" width="70px">
                                 0.00
                                </td>
                                <td class="td_report" style="text-align:right" width="70px">
                                </td>
                                <td class="td_report" style="text-align:right" width="70px">
                                 103,859.45
                                </td>
                                <td class="td_report" style="text-align:right" width="70px">
                                 0.00
                                </td>
                                <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0023761">
                                 <td class="td_report_small" name="transno" tno="PRO00258RRENT0000011" trnid="44765545">
                                  PRO00258
                                  <br/>
                                  RRENT0000011
                                 </td>
                                 <td class="td_report">
                                  INV0023761 - RENT CHARGED
                                 </td>
                                 <td class="td_report">
                                  01/06/2022
                                 </td>
                                 <td class="td_report" style="text-align:right" width="70px">
                                  3,847.80
                                 </td>
                                 <td class="td_report" style="text-align:right" width="70px">
                                  29,499.80
                                 </td>
                                 <td class="td_report" style="text-align:right" width="70px">
                                 </td>
                                 <td class="td_report" style="text-align:right" width="70px">
                                  29,499.80
                                 </td>
                                 <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0024143">
                                  <td class="td_report_small" name="transno" tno="PRO00258RMS0000043" trnid="44767645">
                                   PRO00258
                                   <br/>
                                   RMS0000043
                                  </td>
                                  <td class="td_report">
                                   INV0024143 - ADDITIONAL YARD SPACE
                                  </td>
                                  <td class="td_report">
                                   01/06/2022
                                  </td>
                                  <td class="td_report" style="text-align:right" width="70px">
                                   238.50
                                  </td>
                                  <td class="td_report" style="text-align:right" width="70px">
                                   1,828.50
                                  </td>
                                  <td class="td_report" style="text-align:right" width="70px">
                                  </td>
                                  <td class="td_report" style="text-align:right" width="70px">
                                   31,328.30
                                  </td>
                                  <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0024343">
                                   <td class="td_report_small" name="transno" tno="PRO00258TENMRD0000010" trnid="44768581">
                                    PRO00258
                                    <br/>
                                    TENMRD0000010
                                   </td>
                                   <td class="td_report">
                                    INV0024343 - METER READING FEE
                                   </td>
                                   <td class="td_report">
                                    01/06/2022
                                   </td>
                                   <td class="td_report" style="text-align:right" width="70px">
                                    18.75
                                   </td>
                                   <td class="td_report" style="text-align:right" width="70px">
                                    143.75
                                   </td>
                                   <td class="td_report" style="text-align:right" width="70px">
                                   </td>
                                   <td class="td_report" style="text-align:right" width="70px">
                                    31,472.05
                                   </td>
                                   <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0024454">
                                    <td class="td_report_small" name="transno" tno="PRO00258RMS0000044" trnid="44848190">
                                     PRO00258
                                     <br/>
                                     RMS0000044
                                    </td>
                                    <td class="td_report">
                                     INV0024454 - ELECTRICITY MAXIMUM DEMAND 80 UNITS
                                    </td>
                                    <td class="td_report">
                                     01/06/2022
                                    </td>
                                    <td class="td_report" style="text-align:right" width="70px">
                                     4,844.66
                                    </td>
                                    <td class="td_report" style="text-align:right" width="70px">
                                     37,142.40
                                    </td>
                                    <td class="td_report" style="text-align:right" width="70px">
                                    </td>
                                    <td class="td_report" style="text-align:right" width="70px">
                                     68,614.45
                                    </td>
                                    <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0024456">
                                     <td class="td_report_small" name="transno" tno="PRO00258RMS0000045" trnid="44848196">
                                      PRO00258
                                      <br/>
                                      RMS0000045
                                     </td>
                                     <td class="td_report">
                                      INV0024456 - ELECTRICITY 618792-633256
                                     </td>
                                     <td class="td_report">
                                      01/06/2022
                                     </td>
                                     <td class="td_report" style="text-align:right" width="70px">
                                      3,999.61
                                     </td>
                                     <td class="td_report" style="text-align:right" width="70px">
                                      30,663.68
                                     </td>
                                     <td class="td_report" style="text-align:right" width="70px">
                                     </td>
                                     <td class="td_report" style="text-align:right" width="70px">
                                      99,278.13
                                     </td>
                                     <tr>
                                      <td class="td_report_small" name="transno" tno="PRO00258RENT0000015" trnid="45293830">
                                       PRO00258
                                       <br/>
                                       RENT0000015
                                      </td>
                                      <td class="td_report">
                                       PAYMENT RECEIVED
                                      </td>
                                      <td class="td_report">
                                       06/06/2022
                                      </td>
                                      <td class="td_report" style="text-align:right" width="70px">
                                       0.00
                                      </td>
                                      <td class="td_report" style="text-align:right" width="70px">
                                      </td>
                                      <td class="td_report" style="text-align:right" width="70px">
                                       99,278.13
                                      </td>
                                      <td class="td_report" style="text-align:right" width="70px">
                                       0.00
                                      </td>
                                      <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0025926">
                                       <td class="td_report_small" name="transno" tno="PRO00258RRENT0000012" trnid="45443445">
                                        PRO00258
                                        <br/>
                                        RRENT0000012
                                       </td>
                                       <td class="td_report">
                                        INV0025926 - RENT CHARGED
                                       </td>
                                       <td class="td_report">
                                        01/07/2022
                                       </td>
                                       <td class="td_report" style="text-align:right" width="70px">
                                        3,847.80
                                       </td>
                                       <td class="td_report" style="text-align:right" width="70px">
                                        29,499.80
                                       </td>
                                       <td class="td_report" style="text-align:right" width="70px">
                                       </td>
                                       <td class="td_report" style="text-align:right" width="70px">
                                        29,499.80
                                       </td>
                                       <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0026271">
                                        <td class="td_report_small" name="transno" tno="PRO00258RMS0000046" trnid="45445001">
                                         PRO00258
                                         <br/>
                                         RMS0000046
                                        </td>
                                        <td class="td_report">
                                         INV0026271 - ADDITIONAL YARD SPACE
                                        </td>
                                        <td class="td_report">
                                         01/07/2022
                                        </td>
                                        <td class="td_report" style="text-align:right" width="70px">
                                         238.50
                                        </td>
                                        <td class="td_report" style="text-align:right" width="70px">
                                         1,828.50
                                        </td>
                                        <td class="td_report" style="text-align:right" width="70px">
                                        </td>
                                        <td class="td_report" style="text-align:right" width="70px">
                                         31,328.30
                                        </td>
                                        <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0026463">
                                         <td class="td_report_small" name="transno" tno="PRO00258TENMRD0000011" trnid="45445435">
                                          PRO00258
                                          <br/>
                                          TENMRD0000011
                                         </td>
                                         <td class="td_report">
                                          INV0026463 - METER READING FEE
                                         </td>
                                         <td class="td_report">
                                          01/07/2022
                                         </td>
                                         <td class="td_report" style="text-align:right" width="70px">
                                          18.75
                                         </td>
                                         <td class="td_report" style="text-align:right" width="70px">
                                          143.75
                                         </td>
                                         <td class="td_report" style="text-align:right" width="70px">
                                         </td>
                                         <td class="td_report" style="text-align:right" width="70px">
                                          31,472.05
                                         </td>
                                         <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0026657">
                                          <td class="td_report_small" name="transno" tno="PRO00258RMS0000047" trnid="45463383">
                                           PRO00258
                                           <br/>
                                           RMS0000047
                                          </td>
                                          <td class="td_report">
                                           INV0026657 - WATER
                                          </td>
                                          <td class="td_report">
                                           01/07/2022
                                          </td>
                                          <td class="td_report" style="text-align:right" width="70px">
                                           318.26
                                          </td>
                                          <td class="td_report" style="text-align:right" width="70px">
                                           2,440.00
                                          </td>
                                          <td class="td_report" style="text-align:right" width="70px">
                                          </td>
                                          <td class="td_report" style="text-align:right" width="70px">
                                           33,912.05
                                          </td>
                                          <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0026659">
                                           <td class="td_report_small" name="transno" tno="PRO00258RMS0000048" trnid="45463423">
                                            PRO00258
                                            <br/>
                                            RMS0000048
                                           </td>
                                           <td class="td_report">
                                            INV0026659 - ELECTRICITY MAXIMUM DEMAND 85 UNITS
                                           </td>
                                           <td class="td_report">
                                            01/07/2022
                                           </td>
                                           <td class="td_report" style="text-align:right" width="70px">
                                            5,147.45
                                           </td>
                                           <td class="td_report" style="text-align:right" width="70px">
                                            39,463.80
                                           </td>
                                           <td class="td_report" style="text-align:right" width="70px">
                                           </td>
                                           <td class="td_report" style="text-align:right" width="70px">
                                            73,375.85
                                           </td>
                                           <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0026661">
                                            <td class="td_report_small" name="transno" tno="PRO00258RMS0000049" trnid="45463487">
                                             PRO00258
                                             <br/>
                                             RMS0000049
                                            </td>
                                            <td class="td_report">
                                             INV0026661 - ELECTRICITY 633256-647704
                                            </td>
                                            <td class="td_report">
                                             01/07/2022
                                            </td>
                                            <td class="td_report" style="text-align:right" width="70px">
                                             2,883.32
                                            </td>
                                            <td class="td_report" style="text-align:right" width="70px">
                                             22,105.44
                                            </td>
                                            <td class="td_report" style="text-align:right" width="70px">
                                            </td>
                                            <td class="td_report" style="text-align:right" width="70px">
                                             95,481.29
                                            </td>
                                            <tr>
                                             <td class="td_report_small" name="transno" tno="PRO00258RENT0000016" trnid="45930142">
                                              PRO00258
                                              <br/>
                                              RENT0000016
                                             </td>
                                             <td class="td_report">
                                              PAYMENT RECEIVED
                                             </td>
                                             <td class="td_report">
                                              07/07/2022
                                             </td>
                                             <td class="td_report" style="text-align:right" width="70px">
                                              0.00
                                             </td>
                                             <td class="td_report" style="text-align:right" width="70px">
                                             </td>
                                             <td class="td_report" style="text-align:right" width="70px">
                                              95,481.29
                                             </td>
                                             <td class="td_report" style="text-align:right" width="70px">
                                              0.00
                                             </td>
                                             <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0028842">
                                              <td class="td_report_small" name="transno" tno="PRO00258RMS0000050" trnid="46168952">
                                               PRO00258
                                               <br/>
                                               RMS0000050
                                              </td>
                                              <td class="td_report">
                                               INV0028842 - WATER
                                              </td>
                                              <td class="td_report">
                                               01/08/2022
                                              </td>
                                              <td class="td_report" style="text-align:right" width="70px">
                                               318.26
                                              </td>
                                              <td class="td_report" style="text-align:right" width="70px">
                                               2,440.00
                                              </td>
                                              <td class="td_report" style="text-align:right" width="70px">
                                              </td>
                                              <td class="td_report" style="text-align:right" width="70px">
                                               2,440.00
                                              </td>
                                              <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0028846">
                                               <td class="td_report_small" name="transno" tno="PRO00258RMS0000051" trnid="46168980">
                                                PRO00258
                                                <br/>
                                                RMS0000051
                                               </td>
                                               <td class="td_report">
                                                INV0028846 - ELECTRICITY MAXIMUM DEMAND 88 UNITS
                                               </td>
                                               <td class="td_report">
                                                01/08/2022
                                               </td>
                                               <td class="td_report" style="text-align:right" width="70px">
                                                5,787.91
                                               </td>
                                               <td class="td_report" style="text-align:right" width="70px">
                                                44,374.00
                                               </td>
                                               <td class="td_report" style="text-align:right" width="70px">
                                               </td>
                                               <td class="td_report" style="text-align:right" width="70px">
                                                46,814.00
                                               </td>
                                               <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0028850">
                                                <td class="td_report_small" name="transno" tno="PRO00258RMS0000053" trnid="46169152">
                                                 PRO00258
                                                 <br/>
                                                 RMS0000053
                                                </td>
                                                <td class="td_report">
                                                 INV0028850 - ELECTRICITY 647704-665363
                                                </td>
                                                <td class="td_report">
                                                 01/08/2022
                                                </td>
                                                <td class="td_report" style="text-align:right" width="70px">
                                                 5,389.83
                                                </td>
                                                <td class="td_report" style="text-align:right" width="70px">
                                                 41,322.06
                                                </td>
                                                <td class="td_report" style="text-align:right" width="70px">
                                                </td>
                                                <td class="td_report" style="text-align:right" width="70px">
                                                 88,136.06
                                                </td>
                                                <tr>
                                                 <td class="td_report_small" name="transno" tno="PRO00258GENJIMPTENDEP0000002" trnid="46616512">
                                                  PRO00258
                                                  <br/>
                                                  GENJIMPTENDEP0000002
                                                 </td>
                                                 <td class="td_report">
                                                  OPENING BALANCE IMPORT - TENANT DEPOSIT FROM UNIBASE
                                                 </td>
                                                 <td class="td_report">
                                                  16/08/2022
                                                 </td>
                                                 <td class="td_report" style="text-align:right" width="70px">
                                                  0.00
                                                 </td>
                                                 <td class="td_report" style="text-align:right" width="70px">
                                                  31,350.00
                                                 </td>
                                                 <td class="td_report" style="text-align:right" width="70px">
                                                 </td>
                                                 <td class="td_report" style="text-align:right" width="70px">
                                                  119,486.06
                                                 </td>
                                                 <tr>
                                                  <td class="td_report_small" name="transno" tno="TPRO00258GENJIMPTENDEP0000002" trnid="46616515">
                                                   TPRO0025
                                                   <br/>
                                                   8GENJIMPTENDEP0000002
                                                  </td>
                                                  <td class="td_report">
                                                   OPENING BALANCE IMPORT - TENANT
                                                  </td>
                                                  <td class="td_report">
                                                   16/08/2022
                                                  </td>
                                                  <td class="td_report" style="text-align:right" width="70px">
                                                   0.00
                                                  </td>
                                                  <td class="td_report" style="text-align:right" width="70px">
                                                  </td>
                                                  <td class="td_report" style="text-align:right" width="70px">
                                                   31,350.00
                                                  </td>
                                                  <td class="td_report" style="text-align:right" width="70px">
                                                   88,136.06
                                                  </td>
                                                  <tr>
                                                   <td class="td_report_small" name="transno" tno="PRO00258DEPREF0000001" trnid="46616523">
                                                    PRO00258
                                                    <br/>
                                                    DEPREF0000001
                                                   </td>
                                                   <td class="td_report">
                                                    DEPOSIT REFUND
                                                   </td>
                                                   <td class="td_report">
                                                    16/08/2022
                                                   </td>
                                                   <td class="td_report" style="text-align:right" width="70px">
                                                    0.00
                                                   </td>
                                                   <td class="td_report" style="text-align:right" width="70px">
                                                   </td>
                                                   <td class="td_report" style="text-align:right" width="70px">
                                                    37,953.30
                                                   </td>
                                                   <td class="td_report" style="text-align:right" width="70px">
                                                    50,182.76
                                                   </td>
                                                   <tr>
                                                    <td class="td_report_small" name="transno" tno="PRO00258TENINT0000004" trnid="46646483">
                                                     PRO00258
                                                     <br/>
                                                     TENINT0000004
                                                    </td>
                                                    <td class="td_report">
                                                     INTEREST CHARGED
                                                    </td>
                                                    <td class="td_report">
                                                     31/08/2022
                                                    </td>
                                                    <td class="td_report" style="text-align:right" width="70px">
                                                     0.00
                                                    </td>
                                                    <td class="td_report" style="text-align:right" width="70px">
                                                     1,003.66
                                                    </td>
                                                    <td class="td_report" style="text-align:right" width="70px">
                                                    </td>
                                                    <td class="td_report" style="text-align:right" width="70px">
                                                     51,186.42
                                                    </td>
                                                    <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0030794">
                                                     <td class="td_report_small" name="transno" tno="PRO00258RMS0000056" trnid="46781854">
                                                      PRO00258
                                                      <br/>
                                                      RMS0000056
                                                     </td>
                                                     <td class="td_report">
                                                      INV0030794 - ELECTRICITY MAXIMUM DEMAND 1 UNIT
                                                     </td>
                                                     <td class="td_report">
                                                      01/09/2022
                                                     </td>
                                                     <td class="td_report" style="text-align:right" width="70px">
                                                      63.87
                                                     </td>
                                                     <td class="td_report" style="text-align:right" width="70px">
                                                      489.70
                                                     </td>
                                                     <td class="td_report" style="text-align:right" width="70px">
                                                     </td>
                                                     <td class="td_report" style="text-align:right" width="70px">
                                                      51,676.12
                                                     </td>
                                                     <tr cmou="table_report" cmov="td_report_mouseover" name="trLineClick" slineclick="https://rms.propertysuite.co.za/Reports/Invoices/Invoice.aspx?INV=INV0030796">
                                                      <td class="td_report_small" name="transno" tno="PRO00258RMS0000057" trnid="46781866">
                                                       PRO00258
                                                       <br/>
                                                       RMS0000057
                                                      </td>
                                                      <td class="td_report">
                                                       INV0030796 - ELECTRICITY 665363-665561
                                                      </td>
                                                      <td class="td_report">
                                                       01/09/2022
                                                      </td>
                                                      <td class="td_report" style="text-align:right" width="70px">
                                                       47.52
                                                      </td>
                                                      <td class="td_report" style="text-align:right" width="70px">
                                                       364.32
                                                      </td>
                                                      <td class="td_report" style="text-align:right" width="70px">
                                                      </td>
                                                      <td class="td_report" style="text-align:right" width="70px">
                                                       52,040.44
                                                      </td>
                                                      <tr>
                                                       <td class="td_report_small" name="transno" tno="PRO00258TENINT0000005" trnid="47336651">
                                                        PRO00258
                                                        <br/>
                                                        TENINT0000005
                                                       </td>
                                                       <td class="td_report">
                                                        INTEREST CHARGED
                                                       </td>
                                                       <td class="td_report">
                                                        30/09/2022
                                                       </td>
                                                       <td class="td_report" style="text-align:right" width="70px">
                                                        0.00
                                                       </td>
                                                       <td class="td_report" style="text-align:right" width="70px">
                                                        1,040.81
                                                       </td>
                                                       <td class="td_report" style="text-align:right" width="70px">
                                                       </td>
                                                       <td class="td_report" style="text-align:right" width="70px">
                                                        53,081.25
                                                       </td>
                                                       <tr>
                                                        <td class="td_report_small" name="transno" tno="PRO00258TENINT0000006" trnid="47948527">
                                                         PRO00258
                                                         <br/>
                                                         TENINT0000006
                                                        </td>
                                                        <td class="td_report">
                                                         INTEREST CHARGED
                                                        </td>
                                                        <td class="td_report">
                                                         31/10/2022
                                                        </td>
                                                        <td class="td_report" style="text-align:right" width="70px">
                                                         0.00
                                                        </td>
                                                        <td class="td_report" style="text-align:right" width="70px">
                                                         1,061.63
                                                        </td>
                                                        <td class="td_report" style="text-align:right" width="70px">
                                                        </td>
                                                        <td class="td_report" style="text-align:right" width="70px">
                                                         54,142.88
                                                        </td>
                                                        <tr>
                                                         <td class="td_report_small" name="transno" tno="PRO00258TENINT0000007" trnid="48640686">
                                                          PRO00258
                                                          <br/>
                                                          TENINT0000007
                                                         </td>
                                                         <td class="td_report">
                                                          INTEREST CHARGED
                                                         </td>
                                                         <td class="td_report">
                                                          30/11/2022
                                                         </td>
                                                         <td class="td_report" style="text-align:right" width="70px">
                                                          0.00
                                                         </td>
                                                         <td class="td_report" style="text-align:right" width="70px">
                                                          1,082.86
                                                         </td>
                                                         <td class="td_report" style="text-align:right" width="70px">
                                                         </td>
                                                         <td class="td_report" style="text-align:right" width="70px">
                                                          55,225.74
                                                         </td>
                                                         <tr>
                                                          <td class="td_report_small" name="transno" tno="PRO00258TENINT0000008" trnid="49321600">
                                                           PRO00258
                                                           <br/>
                                                           TENINT0000008
                                                          </td>
                                                          <td class="td_report">
                                                           INTEREST CHARGED
                                                          </td>
                                                          <td class="td_report">
                                                           31/12/2022
                                                          </td>
                                                          <td class="td_report" style="text-align:right" width="70px">
                                                           0.00
                                                          </td>
                                                          <td class="td_report" style="text-align:right" width="70px">
                                                           1,104.51
                                                          </td>
                                                          <td class="td_report" style="text-align:right" width="70px">
                                                          </td>
                                                          <td class="td_report" style="text-align:right" width="70px">
                                                           56,330.25
                                                          </td>
                                                          <tr>
                                                           <td class="td_report_small" name="transno" tno="PRO00258TENINT0000009" trnid="49961674">
                                                            PRO00258
                                                            <br/>
                                                            TENINT0000009
                                                           </td>
                                                           <td class="td_report">
                                                            INTEREST CHARGED
                                                           </td>
                                                           <td class="td_report">
                                                            31/01/2023
                                                           </td>
                                                           <td class="td_report" style="text-align:right" width="70px">
                                                            0.00
                                                           </td>
                                                           <td class="td_report" style="text-align:right" width="70px">
                                                            1,126.61
                                                           </td>
                                                           <td class="td_report" style="text-align:right" width="70px">
                                                           </td>
                                                           <td class="td_report" style="text-align:right" width="70px">
                                                            57,456.86
                                                           </td>
                                                           <tr>
                                                            <td class="td_report_small" name="transno" tno="PRO00258TENINT0000010" trnid="50672083">
                                                             PRO00258
                                                             <br/>
                                                             TENINT0000010
                                                            </td>
                                                            <td class="td_report">
                                                             INTEREST CHARGED
                                                            </td>
                                                            <td class="td_report">
                                                             28/02/2023
                                                            </td>
                                                            <td class="td_report" style="text-align:right" width="70px">
                                                             0.00
                                                            </td>
                                                            <td class="td_report" style="text-align:right" width="70px">
                                                             1,149.14
                                                            </td>
                                                            <td class="td_report" style="text-align:right" width="70px">
                                                            </td>
                                                            <td class="td_report" style="text-align:right" width="70px">
                                                             58,606.00
                                                            </td>
                                                           </tr>
                                                          </tr>
                                                         </tr>
                                                        </tr>
                                                       </tr>
                                                      </tr>
                                                     </tr>
                                                    </tr>
                                                   </tr>
                                                  </tr>
                                                 </tr>
                                                </tr>
                                               </tr>
                                              </tr>
                                             </tr>
                                            </tr>
                                           </tr>
                                          </tr>
                                         </tr>
                                        </tr>
                                       </tr>
                                      </tr>
                                     </tr>
                                    </tr>
                                   </tr>
                                  </tr>
                                 </tr>
                                </tr>
                               </tr>
                              </tr>
                             </tr>
                            </tr>
                           </tr>
                          </tr>
                         </tr>
                        </tr>
                       </tr>
                      </tr>
                     </tr>
                    </tr>
                   </tr>
                  </tr>
                 </tr>
                </tr>
               </tr>
              </tr>
             </tr>
            </tr>
           </tr>
          </table>
         </div>
         <div style="text-align:right; float:right ">
          <table border="1" class="table_report">
           <tr>
            <th class="td_report" style="text-align:left">
             SUBTOTALS
            </th>
            <th class="td_report" style="text-align:right" width="70px">
             74,283.60
            </th>
            <th class="td_report" style="text-align:right" width="70px">
             611,468.40
            </th>
            <th class="td_report" style="text-align:right" width="70px">
             552,862.40
            </th>
            <th class="td_report" style="text-align:right" width="70px">
             58,606.00
            </th>
           </tr>
           <tr>
            <th class="td_report" colspan="4" style="text-align:left">
             DUE BY YOU
            </th>
            <th class="td_report" style="text-align:right" width="70px">
             58,606.00
            </th>
           </tr>
          </table>
         </div>
        </div>
        <div id="ctl00_ContentPlaceHolder1_pTENDepositNONE">
         <br>
          <br>
           <br>
            <div>
            </div>
            <p>
             <span style="font-size:16px">
              <span style="color:rgb(255, 0, 0)">
               <strong>
                Please use TEN00005 when making payments
               </strong>
              </span>
             </span>
            </p>
            <table align="left" style="width:500px">
             <caption>
              <p style="text-align:left">
               <span style="color:rgb(255, 0, 0)">
                <strong>
                 BANKING DETAILS
                </strong>
               </span>
              </p>
             </caption>
             <tbody>
              <tr>
               <td>
                BANK
               </td>
               <td>
                FNB
               </td>
              </tr>
              <tr>
               <td>
                BRANCH CODE
               </td>
               <td>
                250 655
               </td>
              </tr>
              <tr>
               <td>
                ACCOUNT NAME
               </td>
               <td>
                GARY MANN ESTATES
               </td>
              </tr>
              <tr>
               <td>
                ACCOUNT NUMBER
               </td>
               <td>
                62845716432
               </td>
              </tr>
             </tbody>
            </table>
            <p>
            </p>
            <br>
            </br>
           </br>
          </br>
         </br>
        </div>
       </div>
       <input id="ctl00_ContentPlaceHolder1_hidDate" name="ctl00$ContentPlaceHolder1$hidDate" type="hidden"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENAdminID" name="ctl00$ContentPlaceHolder1$hidTENAdminID" type="hidden" value="TEN00005"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENAdminID_display" name="ctl00$ContentPlaceHolder1$hidTENAdminID_display" type="hidden" value="TEN00005 - 00079"/>
       <input id="ctl00_ContentPlaceHolder1_hidOWNAdminID" name="ctl00$ContentPlaceHolder1$hidOWNAdminID" type="hidden" value="OWN00079"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENOldRef" name="ctl00$ContentPlaceHolder1$hidTENOldRef" type="hidden" value="1948*6;1948*8;1948*10 "/>
       <input id="ctl00_ContentPlaceHolder1_hidTENExternalRef" name="ctl00$ContentPlaceHolder1$hidTENExternalRef" type="hidden" value="1948*6;1948*8;1948*10 "/>
       <input id="ctl00_ContentPlaceHolder1_hidTENAddress" name="ctl00$ContentPlaceHolder1$hidTENAddress" type="hidden" value="Anchor Pallets (pty) Ltd, &lt;br&gt;"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENProperty" name="ctl00$ContentPlaceHolder1$hidTENProperty" type="hidden" value="OLIVE BRANCH PARK EX2 Unit 10 &amp; 11"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENStatementVersion" name="ctl00$ContentPlaceHolder1$hidTENStatementVersion" type="hidden" value="VERSION02"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDepositVersion" name="ctl00$ContentPlaceHolder1$hidTENDepositVersion" type="hidden" value="VERSION04"/>
       <input id="ctl00_ContentPlaceHolder1_hidACCAdminID" name="ctl00$ContentPlaceHolder1$hidACCAdminID" type="hidden" value="TEN00005"/>
       <input id="ctl00_ContentPlaceHolder1_hidPROAdminID" name="ctl00$ContentPlaceHolder1$hidPROAdminID" type="hidden" value="PRO00258"/>
       <input id="ctl00_ContentPlaceHolder1_hidStartDate" name="ctl00$ContentPlaceHolder1$hidStartDate" type="hidden" value="01032022"/>
       <input id="ctl00_ContentPlaceHolder1_hidFriendlyStartDate" name="ctl00$ContentPlaceHolder1$hidFriendlyStartDate" type="hidden" value="01/03/2022"/>
       <input id="ctl00_ContentPlaceHolder1_hidEndDate" name="ctl00$ContentPlaceHolder1$hidEndDate" type="hidden" value="28022023"/>
       <input id="ctl00_ContentPlaceHolder1_hidFriendlyEndDate" name="ctl00$ContentPlaceHolder1$hidFriendlyEndDate" type="hidden" value="28/02/2023"/>
       <input id="ctl00_ContentPlaceHolder1_hidIncludeFullDetail" name="ctl00$ContentPlaceHolder1$hidIncludeFullDetail" type="hidden" value="NO"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENOpenBal" name="ctl00$ContentPlaceHolder1$hidTENOpenBal" type="hidden" value="3,041.44"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENOpenBalDescription" name="ctl00$ContentPlaceHolder1$hidTENOpenBalDescription" type="hidden" value="Previous Balance Due by You"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENOpenBalDT" name="ctl00$ContentPlaceHolder1$hidTENOpenBalDT" type="hidden" value="3,041.44"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENOpenBalCR" name="ctl00$ContentPlaceHolder1$hidTENOpenBalCR" type="hidden" value="&amp;nbsp;"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENOpenDate" name="ctl00$ContentPlaceHolder1$hidTENOpenDate" type="hidden" value="01/03/2022"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENTotDT" name="ctl00$ContentPlaceHolder1$hidTENTotDT" type="hidden" value="611,468.40"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENTotCR" name="ctl00$ContentPlaceHolder1$hidTENTotCR" type="hidden" value="552,862.40"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENBalVAT" name="ctl00$ContentPlaceHolder1$hidTENBalVAT" type="hidden" value="74,283.60"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENBalDT" name="ctl00$ContentPlaceHolder1$hidTENBalDT" type="hidden" value="58,606.00"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENBalCR" name="ctl00$ContentPlaceHolder1$hidTENBalCR" type="hidden" value="&amp;nbsp;"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENBal" name="ctl00$ContentPlaceHolder1$hidTENBal" type="hidden" value="58,606.00"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENBalMessage" name="ctl00$ContentPlaceHolder1$hidTENBalMessage" type="hidden" value="DUE BY YOU"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDepRequiredDT" name="ctl00$ContentPlaceHolder1$hidTENDepRequiredDT" type="hidden" value="6,603.30"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDepRequiredCR" name="ctl00$ContentPlaceHolder1$hidTENDepRequiredCR" type="hidden" value="&amp;nbsp;"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDepLineBalDT" name="ctl00$ContentPlaceHolder1$hidTENDepLineBalDT" type="hidden" value="0.00"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDepLineBalCR" name="ctl00$ContentPlaceHolder1$hidTENDepLineBalCR" type="hidden" value="&amp;nbsp;"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDepLineBal" name="ctl00$ContentPlaceHolder1$hidTENDepLineBal" type="hidden" value="0.00"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPTotDT" name="ctl00$ContentPlaceHolder1$hidTENDEPTotDT" type="hidden" value="6,603.30"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPTotCR" name="ctl00$ContentPlaceHolder1$hidTENDEPTotCR" type="hidden" value="0.00"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPBalDT" name="ctl00$ContentPlaceHolder1$hidTENDEPBalDT" type="hidden" value="6,603.30"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPBalCR" name="ctl00$ContentPlaceHolder1$hidTENDEPBalCR" type="hidden" value="&amp;nbsp;"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPMessage" name="ctl00$ContentPlaceHolder1$hidTENDEPMessage" type="hidden" value="Your deposit account is outstanding with R 6,603.30 according to this system."/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPBal" name="ctl00$ContentPlaceHolder1$hidTENDEPBal" type="hidden"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPBalMessageStyle" name="ctl00$ContentPlaceHolder1$hidTENDEPBalMessageStyle" type="hidden"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPBalMessageStylePart" name="ctl00$ContentPlaceHolder1$hidTENDEPBalMessageStylePart" type="hidden"/>
       <input id="ctl00_ContentPlaceHolder1_hidTENDEPBalMessageAppend" name="ctl00$ContentPlaceHolder1$hidTENDEPBalMessageAppend" type="hidden"/>
       <img alt="letterfoot" src="https://rms.propertysuite.co.za/Images/Display.aspx?SOURCE=Company&amp;HF=F&amp;CID=557"/>
       <input id="hidBaseURL" type="hidden" value="https://rms.propertysuite.co.za/"/>
       <input id="hidIsMobile" type="hidden" value="False"/>
       <input id="hidLocale" type="hidden" value="ZA"/>
       <script src="https://rms.propertysuite.co.za/script/MooTools-Core-1.6.0-compat.js" type="text/javascript">
       </script>
       <script src="https://rms.propertysuite.co.za/script/MooTools-More-1.6.0-compat.js" type="text/javascript">
       </script>
       <script src="https://rms.propertysuite.co.za/script/Meio.Mask.js" type="text/javascript">
       </script>
       <script src="https://rms.propertysuite.co.za/script/Meio.Mask.Fixed_001.js" type="text/javascript">
       </script>
       <script src="https://rms.propertysuite.co.za/script/Meio.Mask.Extras.js" type="text/javascript">
       </script>
       <script type="text/javascript">
        var xModalTop='35%';var xModalLeft='35%';var xPOTChooserType='search';
       </script>
       <script src="https://rms.propertysuite.co.za/AJAX_Source/ReportAJAX_A_008.js?v=014" type="text/javascript">
       </script>
      </div>
     </form>
    </td>
   </tr>
  </table>
 </body>

</html>
"""

css = """

<style type="text/css">
@page {{
    size: A4;
    margin: 1cm;
}}

td, th {
    margin: 2px;
    padding: 2px;
}

img {
    width: 100%;
}

 </style>
"""

def generate_pdf(html_content, owner, tenant, property, start, end) -> ContentFile:
    new_html = re.sub(r'width[:=]\s*"\d+px"|width:\s*\d+px;', '', html_content)
    new_html = re.sub(r'font-size\s*:[^;]+;', '', new_html)
    new_html = re.sub(r'<div[^>]*style\s*=\s*"[^"]*font-size:larger;[^"]*">\s*<center>\s*TENANT STATEMENT / TAX INVOICE\s*</center>\s*</div>', '', new_html, flags=re.DOTALL)

    new_html = f"{new_html}\n{css}"
    pdf_file = BytesIO()
    pisa.CreatePDF(new_html, dest=pdf_file)
    pdf_file.seek(0)
    file = ContentFile(pdf_file.getvalue()) #in memory pdf
    file_path = f"statements/{owner}/{tenant}-{property} {start} to {end}.pdf"  # Replace with your desired file path and name
    with open(file_path, "wb") as pdf_file:
        pdf_file.write(file.read())

# generate_pdf(html, "OWN00079", "tenant", "property", "start", "end")
# pdf_content = generate_pdf(html)  # Replace with your HTML content

# Save the PDF to a file

