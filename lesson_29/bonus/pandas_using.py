from pandas import read_excel, read_csv, read_sql, read_json, DataFrame
import psycopg2
# df_original = read_csv("/Users/milanstar/Downloads/test_csv.csv")              # стандарт
#
# dt_dict = df_original.to_dict(orient="records")
# dt_dict[4]['COUNTRY_FROM'] = "Ukraine"
# df_modified = DataFrame(dt_dict)
# df_modified.to_csv("/Users/milanstar/Downloads/test_csv_modified.csv", index=False)
# modified_csv = dt_dict
# print(df_original.compare(df_modified))

# ------------------------------------------


# df_original = read_excel("/Users/milanstar/Downloads/test_excel.xls")
#
# df_dict  = df_original.to_dict(orient="records")
#
# print(df_dict)


# ----------------------------

# conn = psycopg2.connect(
#     dbname="your_database",
#     user="your_user",
#     password="your_password",
#     host="localhost",
#     port="5432"
# )
#
# # Виконання SQL-запиту та отримання результату у вигляді DataFrame
# query = "SELECT id, description, amount, oper_type, iban FROM bank_statements LIMIT 10;"
# df = read_sql(query, conn)
#
#
# # Закриття з'єднання
# conn.close()
#
# # ---------------------------------
#
# df = read_json("../../test_json.json")
# print(df.to_dict(orient="records"))
#
# # ----------------------------------
#
response_data = [
    {"iban": "GE123", "amount": 100, "status": "success"},
    {"iban": "GE456", "amount": 200, "status": "failed"}
]

df = DataFrame(response_data)
assert (df["status"] == "success").any()   # перевірка, що є хоча б одна успішна