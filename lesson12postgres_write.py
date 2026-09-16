import psycopg

connection = psycopg.connect(
    host="localhost",
    dbname="python_automation",
    user="postgres",
    password="tushar123"
)

cursor = connection.cursor()

cursor.execute("INSERT INTO employees(name, salary, title)VALUES ('Raghav', 210000, 'Product Manager'), ('Vishnu' , 90000, 'Senior Data Analyst');")

connection.commit()
print("Data inserted successfully!")

connection.close()