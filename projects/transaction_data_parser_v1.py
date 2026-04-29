# Sample transaction dataset
transactions = [
    {"id": 1, "amount": 5000, "type": "debit"},
    {"id": 2, "amount": 15000, "type": "credit"},
    {"id": 3, "amount": 25000, "type": "debit"},
    {"id": 4, "amount": 8000, "type": "credit"}
]

threshold = 10000
total_amount = 0
debit_total = 0
credit_total = 0

print("High Value Transactions:")

for txn in transactions:
    total_amount += txn["amount"]

    if txn["type"] == "debit":
        debit_total += txn["amount"]
    else:
        credit_total += txn["amount"]

    if txn["amount"] > threshold:
        print(
            f"Transaction ID: {txn['id']} | Amount: {txn['amount']} | Type: {txn['type']}"
        )

print("\nSummary:")
print("Total Transaction Amount:", total_amount)
print("Total Debit Amount:", debit_total)
print("Total Credit Amount:", credit_total)