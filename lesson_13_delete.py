import psycopg

connection = psycopg.connect(
    host="localhost",
    dbname="python_automation",
    user="postgres",
    password="tushar123"
)

cursor = connection.cursor()
name = input("Enter the name of the employee you want to delete: ")
cursor.execute("DELETE FROM employees WHERE name = %s;", (name,))
connection.commit()

print("Data deleted successfully!")
connection.close()
