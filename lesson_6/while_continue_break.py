# while
from random import random

counter = 0
while counter < 10: # while <condition> == True
    print(counter)
    counter = counter + 1 # counter = counter + 1 (+=)


# while True:
#     print("cycle is going")


secret = 10
guess = 0

# while True:
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess == secret:
#         print("You guessed right!")
#         break # break the cycle


number = 0
while number <= 10:
    number += 1
    if number % 2 == 0:
        continue # skip this iteration
    print(f"{number} is an not even number.")

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

# process all not failed transactions
for transaction in transactions_data:
    if transaction['status'] == 'failed':
        continue # not breaking the cycle (just skip this iteration)
    #db_client.process_transaction(transaction)
else:
    print("ELSE")


# if no one failed transactions - send some mark in db
for transaction in transactions_data:
    if transaction['status'] == 'failed':
        break
else:
    print("ELSE")
    # db_client.mark_transactions_as_finished(transactions_data)


#