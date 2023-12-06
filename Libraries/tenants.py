import pyperclip
from steele import data

formatted_list = []

for obj in data:
    tenant = obj["Tenant"]
    prop = obj["Property"]
    transactions = obj["Transactions"]

    for transaction in transactions:
        vat = transaction['vat'].replace(",", "")
        if vat:
            vat = float(vat)
        else:
            vat = 0
        formatted_transaction = (
            f"{transaction['date']},"
            f"{tenant},"
            f"{prop},"
            f"{transaction['description']},"
            f"{transaction['amount']},"
            f"{vat}"
        )
        formatted_list.append(formatted_transaction)

# Join the formatted transactions into a single string separated by newline characters
result = '\n'.join(formatted_list)
pyperclip.copy(result)