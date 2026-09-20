from db import get_connection

import psycopg

conn = get_connection()
print("Connected successfully!")

curr= conn.cursor()
curr.execute("SELECT name , salary FROM employees;")
rows = curr.fetchall()
for row in rows:
    print(f"Name: {row[0]}, Salary: {row[1]}")

conn.close()