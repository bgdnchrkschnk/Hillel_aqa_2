counter = 1
while counter <= 5:
    print(f"Крок {counter}")
    counter += 1

secret = 7
guess = 0

while True:
    guess = int(input("Введи число від 1 до 10: "))
    if guess == secret:
        print("Вгадав!")
        break
    print("Спробуй ще.")




number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(f"Непарне число: {number}")






transactions_data: list[dict] = [
    {"tran_id": 26772, "amount": 120.50, "user_id": 30, "status": "completed"},
    {"tran_id": 26773, "amount": -40.50, "user_id": 22, "status": "pending"},
    {"tran_id": 26771, "amount": -0.50, "user_id": 21, "status": "failed"},
    {"tran_id": 26774, "amount": 75.00, "user_id": 18, "status": "completed"},
    {"tran_id": 26775, "amount": -15.25, "user_id": 25, "status": "pending"},
    {"tran_id": 26776, "amount": 200.00, "user_id": 30, "status": "completed"},
    {"tran_id": 26777, "amount": -5.00, "user_id": 19, "status": "failed"},
    {"tran_id": 26778, "amount": 60.00, "user_id": 22, "status": "completed"},
    {"tran_id": 26779, "amount": -100.00, "user_id": 31, "status": "pending"},
    {"tran_id": 26780, "amount": 300.00, "user_id": 30, "status": "completed"},
    {"tran_id": 26781, "amount": -0.99, "user_id": 21, "status": "failed"},
    {"tran_id": 26782, "amount": 45.75, "user_id": 25, "status": "completed"},
    {"tran_id": 26783, "amount": -20.00, "user_id": 19, "status": "pending"},
    {"tran_id": 26784, "amount": 150.00, "user_id": 18, "status": "completed"},
    {"tran_id": 26785, "amount": -10.00, "user_id": 31, "status": "failed"}
]

# ------------------ break
i = 0
while i < len(transactions_data):
    tran = transactions_data[i]
    if tran["status"] == "failed":
        print(f"Знайдено помилкову транзакцію: {tran['tran_id']}")
        break
    i += 1

# ------------------ continue
i = 0
while i < len(transactions_data):
    tran = transactions_data[i]
    if tran["status"] == "pending":
        i += 1
        continue  # Пропускаємо обробку цієї транзакції
    print(f"Обробка транзакції #{tran['tran_id']} — статус: {tran['status']}")
    i += 1


for transaction in transactions_data:
    if transaction["status"] == "failed":
        continue  # пропускаємо обробку невдалих транзакцій

    print(f"Обробляється транзакція {transaction['tran_id']} на суму {transaction['amount']}")

for transaction in transactions_data:
    if transaction["amount"] > 250:
        print(f"Знайдено велику транзакцію: {transaction['tran_id']} на суму {transaction['amount']}")
        break  # припиняємо цикл після першої великої транзакції

    print(f"Перевірка транзакції {transaction['tran_id']}")