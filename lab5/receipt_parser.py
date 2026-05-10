import re
import json

with open("raw.txt", encoding="utf-8") as f:
    text = f.read()

def parse_amount(raw):
    return float(raw.replace(" ", "").replace(",", "."))

store_match = re.search(r"Филиал\s+(.+)", text)
bin_match = re.search(r"БИН\s+(\d+)", text)
cashier_match = re.search(r"Кассир\s+(.+)", text)
datetime_match = re.search(r"Время:\s+(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})", text)
fiscal_match = re.search(r"Фискальный признак:\s*(\d+)", text)

store = store_match.group(1).strip() if store_match else "N/A"
bin_no = bin_match.group(1) if bin_match else "N/A"
cashier = cashier_match.group(1).strip() if cashier_match else "N/A"
dt = datetime_match.group(1) if datetime_match else "N/A"
fiscal = fiscal_match.group(1) if fiscal_match else "N/A"

payment_match = re.search(r"(Банковская карта|Наличные|Картой):\s*([\d\s]+,\d{2})", text)
total_match = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", text)
vat_match = re.search(r"в т\.ч\. НДС 12%:\s*([\d\s]+,\d{2})", text)

payment_method = payment_match.group(1) if payment_match else "N/A"
payment_amount = parse_amount(payment_match.group(2)) if payment_match else 0.0
total = parse_amount(total_match.group(1)) if total_match else 0.0
vat = parse_amount(vat_match.group(1)) if vat_match else 0.0

all_prices_raw = re.findall(r"\b[\d][\d\s]*,\d{2}\b", text)
all_prices = [parse_amount(p) for p in all_prices_raw]

item_pattern = re.compile(
    r"(\d+)\.\n"
    r"((?:(?!\d+,\d{3}).+\n)+?)"
    r"([\d\s]+,\d{3})\s*x\s*([\d\s]+,\d{2})\n"
    r"([\d\s]+,\d{2})\n"
    r"Стоимость\n"
    r"([\d\s]+,\d{2})",
    re.MULTILINE,
)

items = []
for m in item_pattern.finditer(text):
    number = int(m.group(1))
    name = re.sub(r"\s+", " ", m.group(2)).strip()
    name = re.sub(r"\[RX\]-", "[RX] ", name)
    qty = parse_amount(m.group(3))
    unit_price = parse_amount(m.group(4))
    subtotal = parse_amount(m.group(5))
    items.append({
        "number": number,
        "name": name,
        "quantity": qty,
        "unit_price": unit_price,
        "subtotal": subtotal,
    })

addr_match = re.search(r"г\. .+", text)
address_raw = addr_match.group(0) if addr_match else ""
address_parts = [p.strip() for p in re.split(r",\s*", address_raw)]

calculated_total = sum(i["subtotal"] for i in items)

receipt = {
    "store": store,
    "bin": bin_no,
    "cashier": cashier,
    "datetime": dt,
    "fiscal_id": fiscal,
    "address": address_parts,
    "payment_method": payment_method,
    "payment_amount": payment_amount,
    "vat_12pct": vat,
    "total": total,
    "calculated_total": round(calculated_total, 2),
    "totals_match": abs(calculated_total - total) < 0.01,
    "items": items,
}

print("=" * 60)
print("RECEIPT PARSER")
print("=" * 60)

print("\nStore info (re.search):")
print(f"  Store   : {store}")
print(f"  BIN     : {bin_no}")
print(f"  Cashier : {cashier}")
print(f"  DateTime: {dt}")
print(f"  Fiscal  : {fiscal}")

print("\nPayment info (re.search):")
print(f"  Method : {payment_method}")
print(f"  Amount : {payment_amount:,.2f}")
print(f"  TOTAL  : {total:,.2f}")
print(f"  VAT 12%: {vat:,.2f}")

print("\nAddress (re.split):")
for i, part in enumerate(address_parts, 1):
    print(f"  {i}. {part}")

print("\nAll prices found (re.findall):")
print(f"  Count: {len(all_prices)}")
print(f"  Max: {max(all_prices):,.2f}  Min: {min(all_prices):,.2f}")

print("\nItems (re.finditer + re.sub):")
print(f"  {'#':<4} {'Name':<52} {'Qty':>5} {'Unit':>10} {'Sub':>10}")
print(f"  {'-'*4} {'-'*52} {'-'*5} {'-'*10} {'-'*10}")
for it in items:
    name_trunc = it["name"][:51]
    print(f"  {it['number']:<4} {name_trunc:<52} {it['quantity']:>5.3f} {it['unit_price']:>10,.2f} {it['subtotal']:>10,.2f}")

print(f"\n  Calculated total : {calculated_total:>10,.2f}")
print(f"  Receipt total    : {total:>10,.2f}")
print(f"  Totals match     : {receipt['totals_match']}")

with open("receipt_output.json", "w", encoding="utf-8") as out:
    json.dump(receipt, out, ensure_ascii=False, indent=2)

print("\nSaved to receipt_output.json")
