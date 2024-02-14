const tableContent = document.getElementById('AuthorisationsPaymentsTable_tableContent');
const allDivs = tableContent.querySelectorAll('div');
const matchingDivs = Array.from(allDivs).filter(div => div.id && div.id.match(/^tabelRow_\d+$/));

let total = 0
const extractedData = matchingDivs.map(div => {
  const payment = div.querySelector('.col1 a')?.textContent.trim() || '';
  let amount = div.querySelector('.col3 #Total')?.textContent.trim() || ''; //returns string "#,###.00"

  //need to strip comma and convert to float
  amount = parseFloat(amount.replace(/,/g, ''));
  total += amount
  return { payment, amount };
});

function copyToClipboard(text) {
  const textarea = document.createElement("textarea");
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
}

let data = 'Payment\tAmount\n'
for (let pmt of extractedData) {
  data += `${pmt.payment}\t${pmt.amount}\n`
}
data += `Total\t${total}`

const textarea = document.createElement("textarea");
textarea.value = data;
document.body.appendChild(textarea);
textarea.select();
document.execCommand("copy");
document.body.removeChild(textarea);