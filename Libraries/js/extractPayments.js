function extractAndCopyData() {
  // Select all div elements with the class "tableRowGroupInner"
  const divElements = document.querySelectorAll('div.tableRowGroupInner');

  if (divElements.length > 0) {
    let extractedData = '';
    // Loop through the matched div elements
    divElements.forEach((divElement) => {
      // Extracting data from the div and anchor elements
      const nameElement = divElement.querySelector('div.tableCell.col1')
      const detailsElement = divElement.querySelector('div.tableCell.col2')
      const totalElement = divElement.querySelector('div.tableCell.col3')
      const statusElement = divElement.querySelector('div.tableCell.col4')

      const detailsDateElement = detailsElement.querySelector('div.tableCellItem.doubleItemTop.stack')
      const detailsPaymentMethodElement = detailsElement.querySelector('div.tableCellItem.doubleItemBottom.stack')

      const name = nameElement.textContent.trim();
      const detailsDate = detailsDateElement.textContent.trim();
      const detailsPaymentMethod = detailsPaymentMethodElement.textContent.trim();
      const total = totalElement.textContent.trim();
      const status = statusElement.textContent.trim();

      // Append the extracted data to the result
      extractedData += `${name}\t${detailsDate}\t${detailsPaymentMethod}\t${total}\t${status}\n`;
    });

    // Copy the data to the clipboard
    copyToClipboard(extractedData);

    console.log("Data has been extracted and copied to the clipboard.");
  } else {
    console.log("No div elements with the specified class found.");
  }
}

function copyToClipboard(text) {
  const textarea = document.createElement("textarea");
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
}
