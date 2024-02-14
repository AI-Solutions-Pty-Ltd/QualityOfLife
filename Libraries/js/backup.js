[
  {
    "key": "ctrl+shift+e",
    "label": "extract fnb pre-auth payments",
    "action": "javascript",
    "code": "\n\n  // Select all div elements with the class \"tableRowGroupInner\"\n  const divElements = document.querySelectorAll('div.tableRowGroupInner');\n\n  if (divElements.length > 0) {\n    let extractedData = '';\n    // Loop through the matched div elements\n    divElements.forEach((divElement) => {\n      // Extracting data from the div and anchor elements\n      const nameElement = divElement.querySelector('div.tableCell.col1')\n      const detailsElement = divElement.querySelector('div.tableCell.col2')\n      const totalElement = divElement.querySelector('div.tableCell.col3')\n      const statusElement = divElement.querySelector('div.tableCell.col4')\n\n      const detailsDateElement = detailsElement.querySelector('div.tableCellItem.doubleItemTop.stack')\n      const detailsPaymentMethodElement = detailsElement.querySelector('div.tableCellItem.doubleItemBottom.stack')\n\n      const name = nameElement.textContent.trim();\n      const detailsDate = detailsDateElement.textContent.trim();\n      const detailsPaymentMethod = detailsPaymentMethodElement.textContent.trim();\n      const total = totalElement.textContent.trim();\n      const status = statusElement.textContent.trim();\n\n      // Append the extracted data to the result\n      extractedData += `${name}\\t${detailsDate}\\t${detailsPaymentMethod}\\t${total}\\t${status}\\n`;\n    });\n\n\n  const textarea = document.createElement(\"textarea\");\n  textarea.value = extractedData;\n  document.body.appendChild(textarea);\n  textarea.select();\n  document.execCommand(\"copy\");\n  document.body.removeChild(textarea);\n\n    console.log(\"Data has been extracted and copied to the clipboard.\");\n  } else {\n    console.log(\"No div elements with the specified class found.\");\n  }\n",
    "activeInInputs": true,
    "blacklist": false,
    "sites": "",
    "sitesArray": [
      ""
    ]
  },
  {
    "action": "javascript",
    "code": "alert(\"keep open\")\nsetInterval(() => {\n\n  const continueButton = document.querySelector('a.timeOutContinue');\n  if (continueButton) {\n    continueButton.click();\n  }\n}, 10000);\n",
    "activeInInputs": true,
    "blacklist": false,
    "key": "ctrl+shift+o",
    "label": "keep fnb open",
    "sites": "",
    "sitesArray": [
      ""
    ]
  },
  {
    "action": "javascript",
    "code": "document.querySelectorAll('.shortCutLink')[0].click()",
    "key": "ctrl+shift+a",
    "label": "open fnb accounts",
    "sites": "",
    "sitesArray": [
      ""
    ],
    "activeInInputs": true,
    "blacklist": false
  },
  {
    "key": "ctrl+shift+p",
    "label": "open fnb payments",
    "action": "javascript",
    "code": "document.querySelectorAll('.shortCutLink')[2].click()",
    "activeInInputs": true,
    "blacklist": false,
    "sites": "",
    "sitesArray": [
      ""
    ]
  },
  {
    "action": "javascript",
    "code": "let ele = document.getElementsByClassName(\"eziLink btt_1 eziBtn1_eziLink   \")\n\nfor(let i = 0; i < ele.length; i++) {\n    ele[i].click()\n}",
    "blacklist": false,
    "activeInInputs": true,
    "key": "ctrl+shift+s",
    "label": "submit fnb payments",
    "sites": "",
    "sitesArray": [
      ""
    ]
  },
  {
    "key": "ctrl+alt+e",
    "label": "extract fnb auth payments",
    "action": "javascript",
    "code": "const tableContent = document.getElementById('AuthorisationsPaymentsTable_tableContent');\nconst allDivs = tableContent.querySelectorAll('div');\nconst matchingDivs = Array.from(allDivs).filter(div => div.id && div.id.match(/^tabelRow_\\d+$/));\n\nlet total = 0\nconst extractedData = matchingDivs.map(div => {\n  const payment = div.querySelector('.col1 a')?.textContent.trim() || '';\n  let amount = div.querySelector('.col3 #Total')?.textContent.trim() || ''; //returns string \"#,###.00\"\n\n  //need to strip comma and convert to float\n  amount = parseFloat(amount.replace(/,/g, ''));\n  total += amount\n  return { payment, amount };\n});\n\nfunction copyToClipboard(text) {\n  const textarea = document.createElement(\"textarea\");\n  textarea.value = text;\n  document.body.appendChild(textarea);\n  textarea.select();\n  document.execCommand(\"copy\");\n  document.body.removeChild(textarea);\n}\n\nlet data = 'Payment\\tAmount\\n'\nfor (let pmt of extractedData) {\n  data += `${pmt.payment}\\t${pmt.amount}\\n`\n}\ndata += `Total\\t${total}`\n\ncopyToClipboard(data) ",
    "activeInInputs": true,
    "blacklist": false,
    "sites": "",
    "sitesArray": [
      ""
    ]
  }
]