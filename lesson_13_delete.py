from db import get_connection

connection = get_connection()

cursor = connection.cursor()
name = input("Enter the name of the employee you want to delete: ")
cursor.execute("DELETE FROM employees WHERE name = %s;", (name,))
connection.commit()

print("Data deleted successfully!")
connection.close()
