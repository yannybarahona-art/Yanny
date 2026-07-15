import re

text = "log_entry_09: proc_error %$! item: PRD-9981 priced at $45.99 ... user_id_none.. 23-11-01 end_log"
prod_code_pattern = r"PRD-\d{4}"
prod_code_match = re.search(prod_code_pattern, text)
if prod_code_match:
    print(f"Product code found: {prod_code_match.group()}")

pricing = r"\$\d+\.\d{2}"
pricing_match = re.search(pricing, text)
if pricing_match:
    print(f"Pricing information found: {pricing_match.group()}")

dates = r"\d{2}-\d{2}-\d{2}"
dates_match = re.search(dates, text)
if dates_match:
    print(f"Date information found: {dates_match.group()}")

result = {
    "prodcut_code": prod_code_match.group(),
    "price": pricing_match.group(),
    "date": dates_match.group(),
}
print(f"Result: {result}")
