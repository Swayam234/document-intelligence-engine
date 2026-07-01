import re

def extract_invoice(text):
    data = {}

    amount = re.search(
        r'Total Amount[: ]*₹?\s*(\d+[.,]?\d*)',
        text,
        re.IGNORECASE
    )

    if amount:
        data["Amount"] = amount.group(1)

    date = re.search(
        r'\d{2}/\d{2}/\d{4}',
        text
    )

    if date:
        data["Date"] = date.group()

    vendor = re.search(
        r'Vendor:\s*(.*)',
        text
    )

    if vendor:
        data["Vendor"] = vendor.group(1).strip()

    return data