import pandas as pd
import numpy as np

# # 1. Зі словника списків
# data1 = {
#     "iban": ["GE123", "GE456", "GE789"],
#     "amount": [100, 200, 300],
#     "status": ["success", "failed", "success"]
# }
# df1 = pd.DataFrame(data1)
# print(df1)

# 2. Зі списку словників
data2 = [
    {"iban": "GE123", "amount": 100, "status": "success"},
    {"iban": "GE456", "amount": 200, "status": "failed"},
]
df2 = pd.DataFrame(data2)
print(df2)

# # 3. Зі списку списків + колонок
# data3 = [
#     ["GE123", 100, "success"],
#     ["GE456", 200, "failed"]
# ]
# df3 = pd.DataFrame(data3, columns=["iban", "amount", "status"])
# print(df3)
#
# # 4. З NumPy масиву
# arr = np.array([[1, 2], [3, 4]])
# df4 = pd.DataFrame(arr, columns=["A", "B"])
# print(df4)
#
# # 5. З файлів (CSV, Excel, JSON)
# # df_csv = pd.read_csv("transactions.csv")
# # df_excel = pd.read_excel("transactions.xlsx")
# # df_json = pd.read_json("transactions.json")
#
# # 6. Порожній DataFrame
# df5 = pd.DataFrame(columns=["iban", "amount", "status"])
# print(df5)