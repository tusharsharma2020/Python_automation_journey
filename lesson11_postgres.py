import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="python_automation",
    user="postgres",
    password="tushar123"
)

print("Connected successfully!")

curr= conn.cursor()
curr.execute("SELECT name , salary FROM employees;")
rows = curr.fetchall()
for row in rows:
    print(f"Name: {row[0]}, Salary: {row[1]}")

conn.close()