# data = [
#     {"amount": -50, "category": "food"},
#     {"amount": -20, "category": "transport"},
#     {"amount": 500, "category": "salary"},
#     {"amount": -30, "category": "entertainment"}
# ]
#
# for tx in data:
#     if tx["amount"] > 0:
#         print(f"Income from {tx['category']}: ${tx['amount']}")
#     else:
#         print(f"Expense on {tx['category']}: ${abs(tx['amount'])}")


transactions_data: list[dict] = [
    {
        "tran_id": 26772,
        "amount": 120.50,
        "user_id": 30,
        "status": "completed"
    },
    {
        "tran_id": 26773,
        "amount": -40.50,
        "user_id": 22,
        "status": "pending"
    },
    {
        "tran_id": 26771,
        "amount": -0.50,
        "user_id": 21,
        "status": "failed"
    }
]
income = 0
expenses = 0

completed_transactions: list[dict] = []
other_transactions: list[dict] = []

for tran_data in transactions_data:

    if tran_data.get('status') == 'completed':
        completed_transactions.append(tran_data)
    else:
        other_transactions.append(tran_data)
else: # лише тоді коли цикл успішно пройдений
    print("All transactions analyzed successfully")


print(completed_transactions)
print(other_transactions)


team = ["Den", "Alex", "John"]
working_days = ["Mon", "Tue", "Wed"]

for name in team:

    for working_day in working_days:

        print(f"{name}-{working_day}")